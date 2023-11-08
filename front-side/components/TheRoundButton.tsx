"use client"
import styles from "@/styles/round_button.module.css"
import { useRouter } from "next/navigation";

interface TheButtonInterface{
    image_path: string;
    href: string;
    type: string;
};


const TheButton: React.FC<TheButtonInterface> = ({image_path, href, type}) => {
    const router = useRouter(); 

    // const handleRoute = () =>{
    //     router.push( href );
    // };

    return(
    <div className={styles.button}>
        <div className={styles.content}>
            <img src={image_path} alt={type} />
            <span>{type}</span>
        </div>
    </div>
);
};

export default TheButton;