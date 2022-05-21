​Handling infinite supply :

    generally dimag me ye aata hai infinite supply handle karn ka ki , agar target = 10 hai aur , coin = 2 hai to hm ek loop chalaen 2 ko use karte hue :
    1 + coins used to make 10-(2 * 1)
    2 + coins used to make 10 - (2 * 2)
    .
    .
    .
    .
    
    but ye har denomination ke lie karne ka jarurat nahi hai , jab hm 10 bana rahe honge to already 8 , 6 , 4 , 2 ye sab me v 2 ko use karte hue minimum coin calculate
    kar chuke honge to automatically infinite amount handle ho jaa rha hai by just calling min(dp[2] , 1 + dp[8])
    
    
