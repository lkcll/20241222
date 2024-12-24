import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize page title
st.title("網站Timelapse使用+彰濱工業區的發展")

st.markdown(
    """
    1、針對吳秋生博士的timelapse原始程式碼進行改善，解決Google Earth Engine API Key無法客製化使用的問題
    
    2、加入自訂選取範圍作Timelapse
    
    3、針對衛星影像進行判讀
    """
)
st.title("區域選定")
center = [24.106334, 120.437965]  # 彰濱工業區中心點
zoom = 11  # 設置地圖縮放層級

# 初始化地圖
m = leafmap.Map(minimap_control=True, center=center, zoom=zoom)

# 添加底圖
m.add_basemap("OpenTopoMap")

# GeoJSON 資料
zhangbin_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [120.421143, 24.168995],
                        [120.346298, 24.053048],
                        [120.413246, 24.05148],
                        [120.469208, 24.163356],
                        [120.421143, 24.168995]
                    ]
                ]
            }
        }
    ]
}

# 添加 GeoJSON 資料到地圖
m.add_geojson(zhangbin_geojson, layer_name="彰濱工業區")

# 顯示地圖
m.to_streamlit(height=500)
