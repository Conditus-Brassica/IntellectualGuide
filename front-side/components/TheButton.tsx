"use client"
import styles from "@/styles/button.module.css"
import { useRouter } from "next/navigation";

interface TheButtonInterface{
    title: string;
    href: string;
};



const TheButton: React.FC<TheButtonInterface> = ({title, href}) => {
    const router = useRouter(); 

    const handleRoute = () =>{
        router.push( href );
    };

    return(
    <div className={styles.button} onClick={handleRoute}>
        <span className={styles.title}>{title}</span>
    </div>
);
};

export default TheButton;