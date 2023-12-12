'use client'
import CustomMarker from "@/components/TheMap";
import Head from "next/head";
import styles from "@/styles/main_page.module.css";
import Map from "@/components/TheMap";
import TheSidePanel from "@/components/TheSidePanel";
import { useState } from "react";
import TheLandmarkCard from "@/components/TheLandmarkCard";
import TheRoutePanel from "@/components/TheRoutePanel";
import ThePopup from "@/components/ThePopup";

export default function MapRoute() {

  const [mapData, setMapData] = useState({
    markers: []
  });

  const [popup, setPopup] = useState(false)

  const [landmark, setLandmark] = useState(false);
  const [route, setRoute] = useState(false)

  const [markerState, setMarkerState] = useState({
    targetMarker: CustomMarker
  })

//   const buildARoute = function () {
//     setRoute((pref: boolean)=> {
//         console.log('route=', pref)
//         pref = true
//         return pref
//     })
//     setLandmark(false)
// }

  return (
    <>
      <Head>
        <title>Составить маршрут</title>
        <meta name="description" content="Страница с интерактивыными жлементами для генерации маршрута для Ваших путешествий по Беларуси." />
        <meta name="keywords" content="" />
      </Head>
      <main className={styles.main_page}>
        <div>
          <TheSidePanel mapData={mapData} setMapData={setMapData} />
          <TheLandmarkCard setLandmark={setLandmark} landmark={landmark} setPopup={setPopup} setRoute={setRoute}/>
          <TheRoutePanel setRoute={setRoute} route={route} mapData={mapData} />
          <Map setMapData={setMapData} markerState={markerState} setMarkerState={setMarkerState} setLandmark={setLandmark} route={route} />
          <ThePopup setLandmark={setLandmark} popup={popup} setRoute={setRoute} setPopup={setPopup} />
        </div>
      </main>
    </>
  )
}