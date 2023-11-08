import styles from "@/styles/sidepanel.module.css" 
import TheRoundButton from "./TheRoundButton";

const TheSidePanel = () => {
    return(
    <div className={styles.panel}>
        <div className={styles.search}>search</div>
        <div className={styles.buttons}>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>
            <TheRoundButton type={"Уа какой кнпка"} image_path={"/museum-svgrepo-com.svg"} href={"none"}/>

        </div>
    </div>
    );
};

export default TheSidePanel;