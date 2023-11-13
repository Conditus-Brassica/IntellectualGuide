'use client'

import styles from "@/styles/sidepanel.module.css" 
import TheRoundButton from "./TheRoundButton";

interface TheSidePanelInterface{
    setMapData: any;
    mapData: any;
};

const TheSidePanel: React.FC <TheSidePanelInterface> = ({ setMapData, mapData }) => {
    
    return(
    <div className={styles.panel}>
        <div className={styles.search}>search</div>
        <div className={styles.buttons}>
            <TheRoundButton type={"museum"} image_path={"/museum-svgrepo-com.svg"} setMapData={setMapData} mapData={mapData}/>
            <TheRoundButton type={"restaurant"} image_path={"/museum-svgrepo-com.svg"} setMapData={setMapData} mapData={mapData}/>
            <TheRoundButton type={"river"} image_path={"/museum-svgrepo-com.svg"} setMapData={setMapData} mapData={mapData}/>
        </div>
    </div>
    );
};

export default TheSidePanel;