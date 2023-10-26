import Head from "next/head";
import styles from "@/styles/main_page.module.css"
import TheButton from "@/components/TheButton";

export default function Home() {
  return (
    <>
      <Head>
        <title>Главная страница</title>
        <meta name="description" content="Главная страница сайта всевозможных генераторов для настольной игры D&D." />
        <meta name="keywords" content="" />
      </Head>
      <main className={styles.main_page}>
        <div className={styles.welcome_block}>
          <h1>✈TRAVELER.AI</h1>
          <h3>Ваш персональный гид по достопримечательностям Беларуси</h3>
          <TheButton title={'Поехали!'} href={'/route'}/>
        </div>
      </main>
    </>
  )
}