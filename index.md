<br><br><br><br>
<h1>Shade Cipher Decoder</h1>

Note: Missing/unknown letters will show up as "_" :)

<h3>Message to be decoded:</h3>

<body>
    <input type="text" placeholder="Type something..." id="top_input">
    <button type="button" onclick="decode_input();">Decode!</button>
    <br> <br>
    <div id="text_top">
    </div>
    
    <br><br>
    <h3>Message to be encoded:</h3>
    <input type="text" placeholder="Type something..." id="bot_input">
    <button type="button" onclick="encode_input();">Encode!</button>
    <br> <br>
    <div id="text_bot">
    </div>
    
    <script>
        var dict = {
        '╡': "a",
        "╢": "b",
        "╖": "c",
        '╕': "d",
        "Ξ": "e",
        "║": "f",
        '╗': "g",
        "╝": "h",
        "╘": "i",
        //'': "j",
        "╛": "k",
        "╞": "l",
        '╟': "m",  //not sure
        "╚": "n",
        "╔": "o",
        "╩": "p",
        //"": "q",
        "╠": "r",
        '═': "s",
        "╬": "t",
        "╧": "u",
        "╨": "v",
        "╫": "w",
        '╤': "x",
        "╥": "y",
        //"": "z",
        " ": " ",
      }
      
        function decode_unput(){
            var input = document.getElementById("top_input").value;
            let output = "";
            for (let i = 0; i < input.length; i++) {                                                              
              if (!(input.charAt(i) in dict)) {
              output += "_";
              } 
              else {
                    output += dict[input.charAt(i)];
              }                                         
            }
            document.getElementById("text_top").innerHTML = "Decoded message: " + output;
        }
        
        function cipher_input(){
            let output = "";
            for (let i = 0; i < input.length; i++) {                                                              
              if (!(input.charAt(i) in dict)) {
              output += "_";
              } 
              else {
                    output += dict[input.charAt(i)];
              }                                         
            }
            document.getElementById("text_bottom").innerHTML = "Decoded message: " + output;
        }
        
                                             
        function getKeyByValue(object, value) {
          return Object.keys(object).find(key => object[key] === value);
        }
    </script>
    
     
    
</body>

