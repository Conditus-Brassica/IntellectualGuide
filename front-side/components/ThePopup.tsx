import TheButton from "./TheButton";
import style from "@/styles/popup.module.css"


interface ThePopup {
    setLandmark: any;
    popup: any;
    setRoute: any;
    setPopup: any;
}

const ThePopup: React.FC<ThePopup> = ({ setLandmark, popup, setRoute, setPopup }) => {
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
                <TheButton title="Составить маршрут!" func={buildARoute} />
            </div>
        </div>}
    </>
    )
}

export default ThePopup