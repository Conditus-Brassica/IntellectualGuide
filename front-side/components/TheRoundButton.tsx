"use client"
import { useState } from "react";
import styles from "@/styles/round_button.module.css"

interface TheButtonInterface{
    image_path: string;
    type: string;
    mapData: any;
    setMapData: any;
};


const TheButton: React.FC<TheButtonInterface> = ({image_path, type, mapData}) => {
    const [buttonState, setButtonState] = useState({
        isPressed: true
      });


    const handlerButtonClick = () =>{
        setButtonState(pref=> {
            pref.isPressed = !pref.isPressed
            return pref
        })

        mapData.markers.forEach(function(drowedMarker: any){
            if(drowedMarker.type == type){
                drowedMarker.setOpacity(buttonState.isPressed? 1 : 0 ) 
            };
        });
    };

    return(
    <div className={styles.button} onClick={handlerButtonClick}>
        <div className={styles.content}>
            <img src={image_path} alt={type} />
            <span>{type}</span>
        </div>
    </div>
);
};

export default TheButton