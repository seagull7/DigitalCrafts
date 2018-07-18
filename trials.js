function CaesarCipher(str, offset) {
    var nstr = ""
    var a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for (i in str){
        nstr += ((a[(a.indexOf(str.charAt(i).toUpperCase()) + 26 - offset) % 26]))
    }
    return nstr
}
    
    
    
console.log(CaesarCipher("GDKKN", 25))