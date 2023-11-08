import Head from "next/head";
import styles from "@/styles/main_page.module.css";
import Map from "@/components/TheMap";
import TheSidePanel from "@/components/TheSidePanel";

export default function MapRoute() {
  return (
    <>
      <Head>
        <title>Составить маршрут</title>
        <meta name="description" content="Страница с интерактивыными жлементами для генерации маршрута для Ваших путешествий по Беларуси." />
        <meta name="keywords" content="" />
      </Head>
      <main className={styles.main_page}>
        <div>
          <TheSidePanel/> 
          <Map/>
        </div>
      </main>
    </>
  )
}