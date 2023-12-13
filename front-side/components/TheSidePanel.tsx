'use client'

import styles from "@/styles/sidepanel.module.css"
import TheRoundButton from "./TheRoundButton";
import { useEffect } from "react";
import { useState } from "react";


interface TheSidePanelInterface {
    setTargetCats: any;
    mapData: any;
    targetCats:any;
};

const getCategories = async function () {
    // const response = await fetch(`https://example.com/data?tl_lat=${tl[0]}&tl_lng=${tl[1]}&dr_lat=${br[0]}&dr_lng=${br[1]}`);
    // const data: string[] = await response.json();
    const data = [
        'museum', 'restaurant', 'river'
    ]

    return data
}


const TheSidePanel: React.FC<TheSidePanelInterface> =  ({ setTargetCats, mapData, targetCats }) => {

    const [categories, setCategories] = useState<string[]>([]);

    useEffect(() => {
      const fetchData = async () => {
        const data = await getCategories();
        setCategories(data);
      };
  
      fetchData();
    }, []);
    

    return (
        <div className={styles.panel}>
            <div className={styles.search}>search</div>
            <div className={styles.buttons}>
                {categories.map((value: string, index: number) => (
                    <div key={index}>
                        <TheRoundButton targetCats={targetCats} type={value}  image_path={`/${value}.svg`} functional='filter' mapData={mapData} setTargetCats={setTargetCats}/>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default TheSidePanel;