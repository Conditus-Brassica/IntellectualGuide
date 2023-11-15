import style from "@/styles/landmark_card.module.css"

const TheLandmarkCard = () =>{
    return(
    <div>
        <div className={style.image}>
            <img src="" alt="" />
        </div>
        <div className={style.name}>
            <h1></h1>
        </div>
        <div className={style.description}>
            <p></p>
        </div>
    </div>
    )
}

export default TheLandmarkCard