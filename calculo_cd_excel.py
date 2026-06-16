import numpy as np
import math
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

g = 9.81

cuadrado = {
    "nombre": "Tanque cuadrado",
    "h0": 0.25, "AT": 0.0056, "A0": 0.000025,
    "fluidos": [
        {"nombre": "Agua",   "path": "datos_experimentales/cuadrado/Datos agua.txt"},
        {"nombre": "Aceite", "path": "datos_experimentales/cuadrado/Datos aceite.txt"},
    ],
}

R_b = 0.057; R_t = 0.0615; h0_j = 0.113
alpha_j = (R_t - R_b) / h0_j
A0_j = math.pi * 0.0025**2

jarra = {
    "nombre": "Jarra (tronco de cono)",
    "h0": h0_j, "AT": None, "A0": A0_j,
    "fluidos": [
        {"nombre": "Agua",   "path": "datos_experimentales/tronco_de_cono/Datos Agua.txt"},
        {"nombre": "Aceite", "path": "datos_experimentales/tronco_de_cono/Datos aceite.txt"},
    ],
}

def parse_datos(filepath):
    t_data, y_data = [], []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            parts = line.replace(',', '.').split('\t')
            if len(parts) >= 3:
                try:
                    t_data.append(float(parts[0]))
                    y_data.append(float(parts[2]))
                except ValueError: continue
    return np.array(t_data), np.array(y_data)

def calc_cd_cuadrado(t, h, h0, AT, A0):
    if h <= 0 or h >= h0 or t <= 0: return None
    k = (math.sqrt(h0) - math.sqrt(h)) / t
    return (k * 2 * AT) / (A0 * math.sqrt(2 * g))

def f_cono(h):
    return (R_b**2 * (math.sqrt(h0_j) - math.sqrt(h))
            + (2/3) * R_b * alpha_j * (h0_j**1.5 - h**1.5)
            + (1/5) * alpha_j**2 * (h0_j**2.5 - h**2.5))

def calc_cd_cono(t, h, h0, A0):
    if h <= 0 or h >= h0 or t <= 0: return None
    f = f_cono(h)
    return (2 * math.pi / (t * A0 * math.sqrt(2 * g))) * f

# Estilos
hdr_font = Font(bold=True, size=11)
title_font = Font(bold=True, size=13)
fluid_font = Font(bold=True, size=12, color="003366")
thin_bd = Border(left=Side('thin'), right=Side('thin'), top=Side('thin'), bottom=Side('thin'))
c_align = Alignment(horizontal='center', vertical='center')

def style_hdr(ws, r, n):
    for c in range(1, n+1):
        cell = ws.cell(row=r, column=c)
        cell.font = hdr_font; cell.alignment = c_align; cell.border = thin_bd

def style_row(ws, r, n):
    for c in range(1, n+1):
        cell = ws.cell(row=r, column=c)
        cell.alignment = c_align; cell.border = thin_bd

wb = Workbook()
wb.remove(wb.active)

for config in [cuadrado, jarra]:
    ws = wb.create_sheet(title=config["nombre"][:31])
    row = 1

    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=6)
    ws.cell(row=row, column=1, value=f"Calculo del coeficiente de descarga - {config['nombre']}").font = title_font
    row += 1
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=6)
    if config["AT"] is not None:
        ws.cell(row=row, column=1, value=f"h0 = {config['h0']} m    AT = {config['AT']} m2    A0 = {config['A0']} m2    g = {g} m/s2")
    else:
        ws.cell(row=row, column=1, value=f"h0 = {config['h0']} m    Rb = {R_b} m    Rt = {R_t} m    A0 = {A0_j:.6f} m2    g = {g} m/s2")
    row += 2

    for fluido in config["fluidos"]:
        t, y = parse_datos(fluido["path"])
        resultados = []
        for i in range(len(t)):
            if config["AT"] is not None:
                cd = calc_cd_cuadrado(t[i], y[i], config["h0"], config["AT"], config["A0"])
            else:
                cd = calc_cd_cono(t[i], y[i], config["h0"], config["A0"])
            if cd is not None and 0 < cd < 2:
                resultados.append((t[i], y[i], cd))

        cd_arr = np.array([r[2] for r in resultados])
        N = len(cd_arr)
        cd_mean = np.mean(cd_arr)
        cd_std = np.std(cd_arr, ddof=1)
        cd_uncert = cd_std / math.sqrt(N)

        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=6)
        ws.cell(row=row, column=1, value=f"Fluido: {fluido['nombre']}").font = fluid_font
        row += 1

        headers = ["#", "t (s)", "h (m)", "Cd", "|Cd - Cd prom|"]
        for j, hdr in enumerate(headers, 1):
            ws.cell(row=row, column=j, value=hdr)
        style_hdr(ws, row, len(headers))
        row += 1

        for i, (tv, hv, cdv) in enumerate(resultados):
            ws.cell(row=row, column=1, value=i + 1)
            ws.cell(row=row, column=2, value=round(tv, 3))
            ws.cell(row=row, column=3, value=round(hv, 5))
            ws.cell(row=row, column=4, value=round(cdv, 4))
            ws.cell(row=row, column=5, value=round(abs(cdv - cd_mean), 4))
            style_row(ws, row, len(headers))
            row += 1

        row += 1
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=6)
        ws.cell(row=row, column=1, value="Estadistica").font = Font(bold=True, size=11)
        row += 1

        stats = [
            ("N (puntos validos)", N),
            ("Cd promedio", cd_mean),
            ("Desviacion estandar (sigma)", cd_std),
            ("Incertidumbre (sigma/raiz(N))", cd_uncert),
            ("Resultado final", f"Cd = {cd_mean:.4f} ± {cd_uncert:.4f}"),
        ]
        for label, value in stats:
            ws.cell(row=row, column=1, value=label).font = Font(bold=True)
            ws.cell(row=row, column=2, value=value if isinstance(value, str) else round(value, 4))
            row += 1

        row += 2

    for col in range(1, 6):
        ws.column_dimensions[get_column_letter(col)].width = 20
    ws.column_dimensions['A'].width = 28

wb.save("calculo_cd_experimental.xlsx")
print("Excel con valores calculados generado: calculo_cd_experimental.xlsx")
