import style from "@/styles/landmark_card.module.css"

import sidepanel_style from "@/styles/sidepanel.module.css"
import TheButton from "./TheButton";
interface TheLandmarkCard {
    markerState: any;
    landmark: any;
    setRoute: any;
}

const TheLandmarkCard: React.FC<TheLandmarkCard> = ({ markerState, landmark, setRoute }) => {
    async function getPointInfo() {
        try {
          const response = await fetch('https://example.com/data');
          const data = await response.json();
          console.log(data);
          return data
        } catch (error) {
          alert("Что-то пошло не так! Проверьте соединение с интернетом!");
        }
      };
   
    const buildARoute = function () {
        setRoute((pref: boolean)=> {
            console.log(pref)
            pref = true
            return pref
        })
    }
    return (<>
        {<div style={{ display: landmark ? 'block' : 'none' }}>
                <div className={sidepanel_style.panel}>
                    <div className={style.image}>
                        <img src="" alt="" />
                    </div>
                    <div className={style.name}>
                        <h3></h3>
                    </div>
                    <div className={style.description}>
                        <p></p>
                    </div>
                    <TheButton title="Построить маршрут!" func={buildARoute} />
                </div>
            </div>
        }
    </>
    )
}

export default TheLandmarkCard