'use client'

import styles from "@/styles/sidepanel.module.css"
import TheRoundButton from "./TheRoundButton";

interface TheSidePanelInterface {
    setMapData: any;
    mapData: any;
};

const getCategories = function () {
    // const response = await fetch(`https://example.com/data?tl_lat=${tl[0]}&tl_lng=${tl[1]}&dr_lat=${br[0]}&dr_lng=${br[1]}`);
    // const data: string[] = await response.json();
    const data = [
        'museum', 'restaurant', 'river'
    ]

    return data
}


const TheSidePanel: React.FC<TheSidePanelInterface> = ({ setMapData, mapData }) => {

    return (
        <div className={styles.panel}>
            <div className={styles.search}>search</div>
            <div className={styles.buttons}>
                {getCategories().map((value: string, index: number) => (
                    <div key={index}>
                        <TheRoundButton type={value}  image_path={`/${value}.svg`} setMapData={setMapData} mapData={mapData} />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default TheSidePanel;