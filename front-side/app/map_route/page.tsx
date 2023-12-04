'use client'
import CustomMarker from "@/components/TheMap";
import Head from "next/head";
import styles from "@/styles/main_page.module.css";
import Map from "@/components/TheMap";
import TheSidePanel from "@/components/TheSidePanel";
import { useState } from "react";
import TheLandmarkCard from "@/components/TheLandmarkCard";

export default function MapRoute() {

  const [mapData, setMapData] = useState({
    markers: {}
  });

  const [landmark, setLandmark] = useState(false);


  const [markerState, setMarkerState] = useState({
    targetMarker: CustomMarker
  })



  return (
    <>
      <Head>
        <title>Составить маршрут</title>
        <meta name="description" content="Страница с интерактивыными жлементами для генерации маршрута для Ваших путешествий по Беларуси." />
        <meta name="keywords" content="" />
      </Head>
      <main className={styles.main_page}>
        <div>
          <TheSidePanel mapData={mapData} setMapData={setMapData}/>
          <TheLandmarkCard markerState={markerState} landmark={landmark}/>
          <Map setMapData={setMapData} markerState={markerState} setMarkerState={setMarkerState} setLandmark={setLandmark}/> 
        </div>
      </main>
    </>
  )
}