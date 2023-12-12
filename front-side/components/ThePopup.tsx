import TheButton from "./TheButton";
import style from "@/styles/popup.module.css"
import TheRoundButton from "./TheRoundButton"


interface ThePopup {
    setLandmark: any;
    popup: any;
    setRoute: any;
    setPopup: any;
    mapData: any;
}

const getCategories = function () {
    // const response = await fetch(`https://example.com/data?tl_lat=${tl[0]}&tl_lng=${tl[1]}&dr_lat=${br[0]}&dr_lng=${br[1]}`);
    // const data: string[] = await response.json();
    const data = [
        'museum', 'restaurant', 'river'
    ]

    return data
}

const ThePopup: React.FC<ThePopup> = ({ setLandmark, popup, setRoute, setPopup, mapData }) => {
    const buildARoute = function () {
        setRoute((pref: boolean) => {
            console.log('route=', pref)
            pref = true
            return pref
        })
        setLandmark(false)
        setPopup(false)
    }
    return (<>
        {<div style={{ display: popup ? 'block' : 'none' }} className={style.popup}>
            <div>
                {getCategories().map((value: string, index: number) => (
                    <div key={index}>
                        <TheRoundButton type={value} image_path={`/${value}.svg`} functional='fetch' mapData={mapData}/>
                    </div>
                ))}
                <TheButton title="Составить маршрут!" func={buildARoute} />
            </div>
        </div>}
    </>
    )
}

export default ThePopup