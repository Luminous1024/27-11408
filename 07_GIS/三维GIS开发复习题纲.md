---
tags:
  - GIS
  - 三维GIS
createTime: 2026-04-23T18:00:00
课程: 三维GIS开发
课程类型: 选择性必修
阶段: 大三下
老师: 段新桥
开始日期: 2026-04-23
结束日期: 2026-04-23
---
# 三维GIS开发（Python）基础通用代码块速查手册（VTK + PyVista 完整对照版）

> **本手册包含以下内容：**
> - 每一行代码均有详细注释，**注释中明确标注变量的英文全称和中文意思**
> - VTK 与 PyVista 双版本对照
> - 涵盖数据读写、几何创建、属性操作、空间查询、量算、三角化、纹理映射、栅格处理等
> - 特别补充了 Shapefile 读取后的完整转换步骤（点、线、面、带洞多边形）
>
> **英文全称/中文意思格式：** `variableName (英文全称: 中文意思)` 或 `functionName (英文全称: 中文意思)`


## 1. 数据读取

### 1.1 读取 VTK 文件（.vtk）

```python
# ===== VTK 方式 =====
import vtk  # Visualization Toolkit (可视化工具包)

# 创建一个 VTK 多边形数据读取器对象 (PolyData Reader)
reader = vtk.vtkPolyDataReader()
# 设置要读取的文件路径 (Set File Name)，参数为字符串
reader.SetFileName("input.vtk")
# 执行读取操作 (Update)，将文件内容读入内存并构建数据管道
reader.Update()
# 从读取器中获取输出的 vtkPolyData 对象 (Get Output)，这是 VTK 中存储面/点云/网格的核心数据结构
polydata = reader.GetOutput()

# ===== PyVista 方式 =====
import pyvista as pv  # PyVista (Python 可视化工具)，VTK 的高级封装

# 直接调用 pv.read() 函数 (read)，参数为文件路径字符串，返回一个 PyVista 的 PolyData 对象
mesh = pv.read("input.vtk")
# 区别：PyVista 自动完成读取和 Update，代码更简洁；VTK 需要显式调用 Update 和 GetOutput。
```

### 1.2 读取 Shapefile 文件（.shp）并转换为 VTK/PyVista 几何

> **说明**：VTK 和 PyVista 本身都不直接支持 Shapefile 读取，因此通常借助 GeoPandas 库读取后，再手动提取几何坐标转换为 VTK/PyVista 对象。

```python
# 第一步：使用 GeoPandas 读取 Shapefile
import geopandas as gpd  # GeoPandas (地理空间数据处理库)
import numpy as np       # NumPy (数值计算库)
import pyvista as pv     # PyVista
import vtk               # VTK

# gpd.read_file() 读取 Shapefile (read file)，参数为文件路径和编码（处理中文属性）
gdf = gpd.read_file("data.shp", encoding='gbk')
# GeoDataFrame (地理数据框架)，包含几何列（geometry）和属性列

# ========== 情况1：点要素（Point / MultiPoint）==========
# 提取所有点的坐标（2D 点，Z 设为 0）
coords = []   # coordinates (坐标列表)
for geom in gdf.geometry:          # geometry (几何对象)
    if geom.geom_type == 'Point':   # geometry type = 点
        coords.append([geom.x, geom.y, 0])   # geom.x (几何的X坐标), geom.y (几何的Y坐标)
    elif geom.geom_type == 'MultiPoint':     # MultiPoint (多点集)
        for pt in geom.geoms:                # geoms (子几何列表)
            coords.append([pt.x, pt.y, 0])

# 转换为 NumPy 数组，形状 (N,3)
points_array = np.array(coords)   # points array (点阵)

# ----- PyVista 方式 -----
point_cloud = pv.PolyData(points_array)   # PolyData (多边形数据)，直接构造点云

# ----- VTK 方式 -----
pts = vtk.vtkPoints()                    # points (点集对象)
for x, y, z in points_array:
    pts.InsertNextPoint(x, y, z)         # Insert Next Point (插入下一点)
verts = vtk.vtkCellArray()               # vertices (顶点单元数组)
for i in range(pts.GetNumberOfPoints()): # Get Number Of Points (获取点数)
    vertex = vtk.vtkVertex()              # Vertex (顶点单元，0维)
    vertex.GetPointIds().SetId(0, i)      # Get Point Ids (获取点索引列表), Set Id (设置索引)
    verts.InsertNextCell(vertex)          # Insert Next Cell (插入下一个单元)
polydata = vtk.vtkPolyData()
polydata.SetPoints(pts)                  # Set Points (设置点集)
polydata.SetVerts(verts)                 # Set Verts (设置顶点单元)

# ========== 情况2：线要素（LineString / MultiLineString）==========
lines_points = []   # lines points (每条线的点坐标列表)
for geom in gdf.geometry:
    if geom.geom_type == 'LineString':
        coords = list(geom.coords)        # coordinates (坐标列表)
        lines_points.append([(x, y, 0) for x, y in coords])
    elif geom.geom_type == 'MultiLineString':
        for line in geom.geoms:           # geoms (子几何列表)
            coords = list(line.coords)
            lines_points.append([(x, y, 0) for x, y in coords])

# ----- PyVista 方式 -----
plotter = pv.Plotter()                   # Plotter (绘图器)
for line_pts in lines_points:
    arr = np.array(line_pts)             # array (数组)
    mesh = pv.PolyData(arr)
    n = len(arr)
    # lines 数组格式：每段线用 [2, start_idx, end_idx] 表示，展平为一维
    lines_arr = np.column_stack([np.full(n-1, 2), np.arange(n-1), np.arange(1, n)]).ravel()
    mesh.lines = lines_arr               # lines (线连接关系)
    plotter.add_mesh(mesh, color='blue', line_width=2)
plotter.show()

# ----- VTK 方式 -----
for line_pts in lines_points:
    pts = vtk.vtkPoints()
    for x, y, z in line_pts:
        pts.InsertNextPoint(x, y, z)
    polyline = vtk.vtkPolyLine()          # PolyLine (折线单元)
    polyline.GetPointIds().SetNumberOfIds(len(line_pts))  # Set Number Of Ids (设置索引数量)
    for i in range(len(line_pts)):
        polyline.GetPointIds().SetId(i, i)
    cells = vtk.vtkCellArray()            # cells (单元数组)
    cells.InsertNextCell(polyline)        # Insert Next Cell (插入下一个单元)
    pd_line = vtk.vtkPolyData()
    pd_line.SetPoints(pts)
    pd_line.SetLines(cells)               # Set Lines (设置线单元)

# ========== 情况3：多边形面要素（Polygon / MultiPolygon，无洞）==========
polygons = []   # polygons (多边形列表)
for geom in gdf.geometry:
    if geom.geom_type == 'Polygon':
        exterior = list(geom.exterior.coords)  # exterior (外环坐标)
        exterior = exterior[:-1]               # 去掉最后一个重复的闭合点
        polygons.append([(x, y, 0) for x, y in exterior])
    elif geom.geom_type == 'MultiPolygon':
        for poly in geom.geoms:
            exterior = list(poly.exterior.coords)[:-1]
            polygons.append([(x, y, 0) for x, y in exterior])

# ----- PyVista 方式 -----
plotter = pv.Plotter()
for poly_pts in polygons:
    points = np.array(poly_pts)
    n = len(points)
    faces = np.hstack([[n], np.arange(n)]).astype(np.int32)  # faces (面片连接数组)
    mesh = pv.PolyData(points, faces)
    mesh = mesh.triangulate()             # triangulate (三角化)
    plotter.add_mesh(mesh, opacity=0.7, color='green')
plotter.show()

# ----- VTK 方式 -----
for poly_pts in polygons:
    pts = vtk.vtkPoints()
    for x, y, z in poly_pts:
        pts.InsertNextPoint(x, y, z)
    polygon = vtk.vtkPolygon()            # Polygon (多边形单元)
    polygon.GetPointIds().SetNumberOfIds(len(poly_pts))
    for i in range(len(poly_pts)):
        polygon.GetPointIds().SetId(i, i)
    cells = vtk.vtkCellArray()
    cells.InsertNextCell(polygon)
    pd_poly = vtk.vtkPolyData()
    pd_poly.SetPoints(pts)
    pd_poly.SetPolys(cells)               # Set Polys (设置多边形单元)
    tri = vtk.vtkTriangleFilter()         # Triangle Filter (三角形过滤器)
    tri.SetInputData(pd_poly)
    tri.Update()
    triangulated = tri.GetOutput()

# ========== 情况4：带洞多边形 ==========
def get_ring_points(ring_coords, z=0):
    """将坐标环转换为点列表，自动去掉闭合重复点"""
    coords = list(ring_coords)
    if len(coords) > 1 and coords[0] == coords[-1]:
        coords = coords[:-1]
    return [(x, y, z) for x, y in coords]

for geom in gdf.geometry:
    if geom.geom_type != 'Polygon':
        continue
    exterior_pts = get_ring_points(geom.exterior.coords)   # exterior points (外环点)
    interior_pts_list = [get_ring_points(ring.coords) for ring in geom.interiors]  # interior (内环)
    
    all_pts = exterior_pts[:]
    for interior in interior_pts_list:
        all_pts.extend(interior)
    
    pts = vtk.vtkPoints()
    for x, y, z in all_pts:
        pts.InsertNextPoint(x, y, z)
    
    cells = vtk.vtkCellArray()
    point_offset = 0   # point offset (点偏移量)
    # 外环单元
    ext_n = len(exterior_pts)
    ext_poly = vtk.vtkPolygon()
    ext_poly.GetPointIds().SetNumberOfIds(ext_n)
    for i in range(ext_n):
        ext_poly.GetPointIds().SetId(i, point_offset + i)
    cells.InsertNextCell(ext_poly)
    point_offset += ext_n
    # 内环单元
    for interior in interior_pts_list:
        int_n = len(interior)
        int_poly = vtk.vtkPolygon()
        int_poly.GetPointIds().SetNumberOfIds(int_n)
        for i in range(int_n):
            int_poly.GetPointIds().SetId(i, point_offset + i)
        cells.InsertNextCell(int_poly)
        point_offset += int_n
    
    pd_hole = vtk.vtkPolyData()
    pd_hole.SetPoints(pts)
    pd_hole.SetPolys(cells)
    # 使用 vtkContourTriangulator (轮廓三角化器) 处理带洞多边形
    tri_filter = vtk.vtkContourTriangulator()
    tri_filter.SetInputData(pd_hole)
    tri_filter.Update()
    triangulated = tri_filter.GetOutput()
    pv_mesh = pv.wrap(triangulated)
    pv_mesh.plot(color='green', show_edges=True)

# ========== 添加属性数据 ==========
values = gdf['value'].values   # values (属性值数组)
# PyVista 方式
point_cloud.point_data['value'] = values   # point_data (点属性数据)
# VTK 方式
arr = vtk.vtkDoubleArray()     # Double Array (双精度数组)
arr.SetName("value")           # Set Name (设置名称)
for val in values:
    arr.InsertNextValue(val)   # Insert Next Value (插入下一个值)
polydata.GetPointData().AddArray(arr)  # Get Point Data (获取点属性数据), Add Array (添加数组)

# 对于线/面要素（单元属性）
mesh.cell_data['line_id'] = line_ids    # cell_data (单元属性数据)
```

### 1.3 读取 CSV 点云数据

```python
import pandas as pd  # Pandas (数据分析库)

# pd.read_csv() 读取 CSV 文件 (read CSV)，返回 DataFrame 对象
df = pd.read_csv("points.csv")
# 从 DataFrame 中提取 'x', 'y', 'z' 列，.values 将 Series 转换为 NumPy 数组
x = df['x'].values   # x (X坐标数组)
y = df['y'].values   # y (Y坐标数组)
z = df['z'].values   # z (Z坐标数组)

import numpy as np
# np.column_stack (column stack，按列堆叠) 将一维数组合并为 (N,3) 二维数组
coords = np.column_stack([x, y, z])

# PyVista 方式
point_cloud = pv.PolyData(coords)
# VTK 方式见 2.1 和 2.2
```

---

## 2. 创建基础几何数据

### 2.1 创建点集（顶点表）

```python
# ===== VTK =====
# vtkPoints (VTK点集对象)，用于存储所有点的三维坐标
points = vtk.vtkPoints()
# zip (拉链函数) 并行遍历 x_list, y_list, z_list
for xi, yi, zi in zip(x_list, y_list, z_list):
    # InsertNextPoint (插入下一点)，参数为三个浮点数坐标
    points.InsertNextPoint(xi, yi, zi)

# ===== PyVista =====
import numpy as np
# np.column_stack (按列堆叠) 合并坐标
coords = np.column_stack([x_list, y_list, z_list])
# pv.PolyData (PolyData对象)，直接从坐标数组构造点云
point_cloud = pv.PolyData(coords)
```

### 2.2 为散点建立拓扑（vtkVertex）

```python
# ===== VTK =====
# vtkCellArray (单元数组)，用于存储所有顶点单元
verts = vtk.vtkCellArray()
# GetNumberOfPoints (获取点数) 返回点数
for i in range(points.GetNumberOfPoints()):
    # vtkVertex (顶点单元)，0维单元，代表孤立点
    vertex = vtk.vtkVertex()
    # GetPointIds (获取点索引列表), SetId (设置索引)，第0个位置设为i
    vertex.GetPointIds().SetId(0, i)
    # InsertNextCell (插入下一个单元)
    verts.InsertNextCell(vertex)

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)     # SetPoints (设置点集)
polydata.SetVerts(verts)       # SetVerts (设置顶点单元)

# ===== PyVista =====
# PyVista 自动处理顶点拓扑，无需手动创建
```

### 2.3 创建折线

```python
# ========== 方法1：多个独立线段 ==========
lines = vtk.vtkCellArray()
for i in range(n-1):
    line = vtk.vtkLine()               # vtkLine (线段单元)
    line.GetPointIds().SetId(0, i)     # SetId (设置索引)，起点
    line.GetPointIds().SetId(1, i+1)   # 终点
    lines.InsertNextCell(line)
polydata.SetLines(lines)               # SetLines (设置线单元)

# ========== 方法2：单条 vtkPolyLine ==========
lines = vtk.vtkCellArray()
polyline = vtk.vtkPolyLine()           # vtkPolyLine (折线单元)
polyline.GetPointIds().SetNumberOfIds(n)  # SetNumberOfIds (设置索引数量)
for i in range(n):
    polyline.GetPointIds().SetId(i, i)
lines.InsertNextCell(polyline)
polydata.SetLines(lines)

# ========== 方法3：vtkPolyLineSource ==========
source = vtk.vtkPolyLineSource()       # vtkPolyLineSource (折线源)
source.SetNumberOfPoints(n)            # SetNumberOfPoints (设置点数)
for i in range(n):
    source.SetPoint(i, x[i], y[i], z[i])  # SetPoint (设置点坐标)
source.Update()
polydata = source.GetOutput()

# ===== PyVista 方式 =====
mesh = pv.PolyData(coords)
# np.full (填充数组)，np.arange (生成等差数组)，np.column_stack (按列堆叠)，ravel (展平)
lines_array = np.column_stack([np.full(n-1, 2), np.arange(n-1), np.arange(1, n)]).ravel()
mesh.lines = lines_array   # lines (线连接关系)
```

### 2.4 创建多边形

```python
# ===== VTK =====
polygon = vtk.vtkPolygon()              # vtkPolygon (多边形单元)
polygon.GetPointIds().SetNumberOfIds(n)
for i in range(n):
    polygon.GetPointIds().SetId(i, i)
cells = vtk.vtkCellArray()
cells.InsertNextCell(polygon)
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetPolys(cells)                # SetPolys (设置多边形单元)

# ===== PyVista =====
mesh = pv.PolyData()
mesh.points = coords                    # points (点坐标)
# np.hstack (水平堆叠)，astype (类型转换)
faces = np.hstack([[n], np.arange(n)]).astype(np.int32)  # faces (面片连接数组)
mesh.faces = faces
```

---

## 3. 数据访问与属性操作

### 3.1 获取点数和单元数

```python
# VTK
n_pts = polydata.GetNumberOfPoints()    # Get Number Of Points (获取点数)
n_cells = polydata.GetNumberOfCells()   # Get Number Of Cells (获取单元数)

# PyVista
n_pts = mesh.n_points   # n_points (点数属性)
n_cells = mesh.n_cells  # n_cells (单元数属性)
```

### 3.2 获取单个点坐标

```python
# VTK
p = [0.0, 0.0, 0.0]   # point (点坐标列表)
polydata.GetPoint(point_id, p)          # GetPoint (获取点坐标)，填充到 p

# PyVista
p = mesh.points[point_id]               # points (点集数组)，返回 NumPy 数组
```

### 3.3 获取一个单元（三角形）的顶点索引

```python
# VTK
idList = vtk.vtkIdList()                # IdList (索引列表)
polydata.GetCellPoints(cell_id, idList)  # GetCellPoints (获取单元的点索引)
v0 = idList.GetId(0)                    # GetId (获取索引)
v1 = idList.GetId(1)
v2 = idList.GetId(2)

# PyVista
cell = mesh.get_cell(cell_id)           # get_cell (获取单元)
p0 = cell.points[0]                     # points (点坐标数组)
p1 = cell.points[1]
p2 = cell.points[2]
```

### 3.4 添加点属性数据

```python
# VTK
arr = vtk.vtkFloatArray()               # FloatArray (浮点数组)
arr.SetName("attribute")                # SetName (设置名称)
for val in values:
    arr.InsertNextValue(val)            # InsertNextValue (插入下一个值)
polydata.GetPointData().AddArray(arr)   # GetPointData (获取点属性数据), AddArray (添加数组)

# PyVista
mesh.point_data["attribute"] = values_array   # point_data (点属性字典)
mesh.set_active_scalars("attribute")          # set_active_scalars (设置活动标量)
```

### 3.5 获取数据边界范围

```python
# VTK
bounds = [0.0]*6   # bounds (边界数组)，[xmin,xmax,ymin,ymax,zmin,zmax]
polydata.GetBounds(bounds)              # GetBounds (获取边界)

# PyVista
bounds = mesh.bounds                    # bounds (边界元组)
```

---

## 4. 三角化与网格处理

### 4.1 三角化（TriangleFilter）

```python
# VTK
tri = vtk.vtkTriangleFilter()           # TriangleFilter (三角形过滤器)
tri.SetInputData(polydata)              # SetInputData (设置输入数据)
tri.Update()
triangulated = tri.GetOutput()

# PyVista
tri_mesh = mesh.triangulate()           # triangulate (三角化方法)
```

### 4.2 Delaunay 三角化

```python
# VTK
delaunay = vtk.vtkDelaunay2D()          # Delaunay2D (Delaunay二维三角化)
delaunay.SetInputData(point_cloud)
delaunay.Update()
tri_mesh = delaunay.GetOutput()

# PyVista
tri_mesh = mesh.delaunay_2d()           # delaunay_2d (Delaunay二维三角化)
```

---

## 5. 空间索引与查询

### 5.1 点定位器（PointLocator）

```python
# VTK
locator = vtk.vtkPointLocator()         # PointLocator (点定位器)
locator.SetDataSet(polydata)            # SetDataSet (设置数据集)
locator.BuildLocator()                  # BuildLocator (构建索引)
nearest_id = locator.FindClosestPoint(query_point)  # FindClosestPoint (查找最近点)

idList = vtk.vtkIdList()
locator.FindPointsWithinRadius(radius, query_point, idList)  # FindPointsWithinRadius (半径内查找)

# PyVista 使用 scipy
from scipy.spatial import KDTree        # KDTree (K维树)
tree = KDTree(mesh.points)
dist, idx = tree.query(query_point, k=1)   # query (查询)，k=1 最近一个
indices = tree.query_ball_point(query_point, r=radius)  # query_ball_point (半径内查询)
```

### 5.2 单元定位器（CellLocator）

```python
# VTK
cellLoc = vtk.vtkCellLocator()          # CellLocator (单元定位器)
cellLoc.SetDataSet(polydata)
cellLoc.BuildLocator()

closest_point = [0.0, 0.0, 0.0]
cellId = vtk.reference(0)               # reference (引用对象，用于输出)
subId = vtk.reference(0)
dist2 = vtk.reference(0.0)
cellLoc.FindClosestPoint(query_point, closest_point, cellId, subId, dist2)

t = vtk.reference(0.0)
intersect_point = [0.0, 0.0, 0.0]
pcoords = [0.0, 0.0, 0.0]
cellLoc.IntersectWithLine(p1, p2, 1e-6, t, intersect_point, pcoords, subId, cellId)

# PyVista
closest_cell = mesh.find_closest_cell(query_point)  # find_closest_cell (查找最近单元)
points, cells = mesh.ray_trace(p1, p2)              # ray_trace (射线求交)
```

---

## 6. 几何量算

### 6.1 三角形面积（三维）

```python
import numpy as np
# p0, p1, p2 为三个顶点坐标 (3,)
edge1 = p1 - p0      # edge1 (边向量1)
edge2 = p2 - p0      # edge2 (边向量2)
cross = np.cross(edge1, edge2)   # cross (叉积)
area_3d = 0.5 * np.linalg.norm(cross)  # norm (模长)
```

### 6.2 三角形面积（投影到 XY 平面）

```python
p0_2d = p0[:2]; p1_2d = p1[:2]; p2_2d = p2[:2]  # 取前两个分量
v1 = p1_2d - p0_2d
v2 = p2_2d - p0_2d
cross_2d = v1[0] * v2[1] - v1[1] * v2[0]  # 二维叉积
area_2d = 0.5 * abs(cross_2d)
```

### 6.3 欧氏距离

```python
import math
d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)  # Euclidean distance (欧氏距离)
# 或
d = np.linalg.norm(p1 - p2)
```

---

## 7. 数据保存

### 7.1 保存为 VTK 文件

```python
# VTK
writer = vtk.vtkPolyDataWriter()        # PolyDataWriter (多边形数据写入器)
writer.SetFileName("output.vtk")        # SetFileName (设置文件名)
writer.SetInputData(polydata)           # SetInputData (设置输入数据)
writer.Write()                          # Write (写入)

# PyVista
mesh.save("output.vtk")                 # save (保存)
```

### 7.2 保存为 VTP 文件

```python
# VTK
writer = vtk.vtkXMLPolyDataWriter()     # XMLPolyDataWriter (XML格式写入器)
writer.SetFileName("output.vtp")
writer.SetInputData(polydata)
writer.Write()

# PyVista
mesh.save("output.vtp")
```

---

## 8. 可视化

### 8.1 简单快速显示

```python
# PyVista
mesh.plot()                              # plot (绘图)
mesh.plot(scalars="attribute", cmap="coolwarm")  # scalars (标量), cmap (颜色映射)
```

### 8.2 使用 Plotter 多子图

```python
plotter = pv.Plotter(shape=(1,2), window_size=(1200,500))  # Plotter (绘图器)
plotter.subplot(0,0)                     # subplot (子图)
plotter.add_mesh(mesh1, color='red', show_edges=True)  # add_mesh (添加网格)
plotter.subplot(0,1)
plotter.add_mesh(mesh2, color='blue', opacity=0.5)     # opacity (透明度)
plotter.add_axes(line_width=2)           # add_axes (添加坐标轴)
plotter.add_text("Title", position='upper_left', font_size=12)  # add_text (添加文字)
plotter.show()
```

---

## 9. 栅格 / 影像基础操作

### 9.1 读取并查看影像信息

```python
# VTK
reader = vtk.vtkPNGReader()              # PNGReader (PNG读取器)
reader.SetFileName("image.png")
reader.Update()
img = reader.GetOutput()
print(img.GetDimensions())               # GetDimensions (获取维度)
print(img.GetOrigin())                   # GetOrigin (获取原点)
print(img.GetSpacing())                  # GetSpacing (获取间距)

# PyVista
img = pv.read("image.png")
print(img.dimensions)                    # dimensions (维度属性)
print(img.origin)                        # origin (原点属性)
print(img.spacing)                       # spacing (间距属性)
```

### 9.2 创建简单画布

```python
canvas = vtk.vtkImageCanvasSource2D()    # ImageCanvasSource2D (2D画布源)
canvas.SetExtent(0, 400, 0, 600, 0, 0)   # SetExtent (设置范围)
canvas.SetScalarTypeToUnsignedChar()     # SetScalarTypeToUnsignedChar (设置标量类型为无符号字符)
canvas.SetNumberOfScalarComponents(3)    # SetNumberOfScalarComponents (设置颜色分量数)
canvas.SetDrawColor(0,0,0)               # SetDrawColor (设置绘制颜色)
canvas.FillBox(0,400,0,600)              # FillBox (填充矩形)
canvas.SetDrawColor(255,0,0)
canvas.FillBox(10,300,10,500)
canvas.Update()

pv_img = pv.ImageData(canvas.GetOutput())
pv_img.plot(rgb=True)                    # rgb (RGB模式)
```

---

## 10. 纹理映射

```python
mesh = pv.read("model.vtk")
texture = pv.read_texture("image.jpg")   # read_texture (读取纹理)
# texture_map_to_plane (纹理映射到平面)，use_bounds (使用包围盒)，inplace (原地修改)
mesh.texture_map_to_plane(use_bounds=True, inplace=True)
plotter = pv.Plotter()
plotter.add_mesh(mesh, texture=texture, smooth_shading=True)  # smooth_shading (平滑着色)
plotter.show()
```

---

## 11. 常用辅助工具

### 11.1 固定随机种子

```python
import numpy as np
np.random.seed(42)   # seed (随机种子)，保证结果可重现
```

### 11.2 遍历所有三角形单元

```python
for cell_id in range(mesh.n_cells):
    cell = mesh.get_cell(cell_id)        # get_cell (获取单元)
    p0, p1, p2 = cell.points[0], cell.points[1], cell.points[2]
    # 进行面积、法向量等计算
```

---

## 12. 总结：VTK 与 PyVista 选用建议

| 场景 | 推荐方式 | 原因 |
|------|----------|------|
| 考试快速编写、展示结果 | **PyVista** | 代码行数少，语法直观 |
| 理解底层原理、回答概念题 | **VTK** | 需要了解 Reader/Filter/Mapper/Actor 流程 |
| 需要精细控制空间查询 | **VTK** | PyVista 封装不够精细 |
| 大规模点云、高性能需求 | **VTK** | 底层控制可优化内存 |
| 纹理映射、多子图可视化 | **PyVista** | 封装完善，代码简洁 |

---