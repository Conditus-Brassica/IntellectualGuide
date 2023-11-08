'use client'

import { useEffect } from 'react';
import L from 'leaflet';
import styles from '@/styles/map.module.css'

async function getPoints() {
  try {
    const response = await fetch('https://example.com/data');
    const data = await response.json();
    console.log(data);
    //Кастомные интерактивные маркеры
  } catch (error) {
    alert("Что-то пошло не так! Проверьте соединение с интернетом!");
  }
}

async function getPointInfo() {
  try {
    const response = await fetch('https://example.com/data');
    const data = await response.json();
    console.log(data);
    //отрисовка карточки достопримечательности
  } catch (error) {
    alert("Что-то пошло не так! Проверьте соединение с интернетом!");
  }
}


const TheMap = () => {
    useEffect(() => {
      const map = L.map('map').setView([51.505, -0.09], 13); 
      var BelarusGeoJSON: any = {
        "type": "FeatureCollection",
        "features": [
          {
            "type": "Feature",
            "properties": {},
            "geometry": { 
              "type": "Polygon",
              "coordinates": [
                [
                  [23.5149129, 53.9760145],
                  [23.9104208, 53.0285526],
                  [23.1523641, 52.2754422],
                  [23.5368856, 51.5229876],
                  [23.9323934, 51.5844674],
                  [25.5803426, 51.9109574],
                  [27.6457723, 51.4614248],
                  [30.5791219, 51.2693639],
                  [30.5901083, 51.611765],
                  [30.9306844, 52.0800705],
                  [31.7986043, 52.1205627],
                  [31.3921102, 53.1934206],
                  [32.1281942, 53.0285526],
                  [32.7104696, 53.3117344],
                  [32.7104696, 53.4689775],
                  [31.150411, 54.648944],
                  [30.9746297, 55.5850737],
                  [30.348409, 55.8449979],
                  [28.1291708, 56.152181],
                  [26.6570028, 55.6842964],
                  [25.8110555, 54.9339821],
                  [25.5363973, 54.3298737],
                  [23.5149129, 53.9760145]
                ]
              ]
            }
          }]}; 
          
      var BelarusLayer: any = L.geoJSON(BelarusGeoJSON);
      map.setView(BelarusLayer.getBounds().getCenter(), 10);
      map.setMaxBounds(BelarusLayer.getBounds())      
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
      }).addTo(map);
      
      // map.on('click', function(e) {
      //   var lat = e.latlng.lat;
      //   var lng = e.latlng.lng;
      //   var marker = L.marker([lat, lng]).addTo(map);
      //   console.log('Координаты клика:', lat, lng);
      // });
  
      return () => {
        map.remove(); // Очистка карты при размонтировании компонента
      };
    }, []);

    
    return <div id="map" className={styles.map}></div>;
  };

  export default TheMap