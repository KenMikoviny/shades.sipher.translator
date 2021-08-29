<h1>Shade Cipher Decoder</h1>

Note: Missing/unknown letters will show up as "_" :)


<h3>Code to be translated:</h3>

<body>
    <input type="text" placeholder="Type something..." id="myInput">
    <button type="button" onclick="getInputValue();">Decode!</button>
    
    
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
        //'╡': "j",
        "╛": "k",
        "╞": "l",
        '╟': "m",  //not sure
        "╚": "n",
        "╔": "o",
        "╩": "p",
        //"╩": "q",
        "╠": "r",
        '═': "s",
        "╬": "t",
        "╧": "u",
        "╨": "v",
        "╫": "w",
        '╤': "x",
        "╥": "y",
        //"╢": "z",
        " ": " ",
      }
      
        function translateInput(input){
            let output = "";
            var myValue = "";
        
            
        
            for (let i = 0; i < input.length; i++) {
                                                                           
              if (!(input.charAt(i) in dict)) {
              output += "_";
              } 
              else {
                    output += dict[input.charAt(i)];
              }                                         
            }
           
            alert("output: " + output);
        }
        
        function getInputValue(){
            // Selecting the input element and get its value 
            var inputVal = document.getElementById("myInput").value;
            translateInput(inputVal);
            
        }
    
    
    </script>
    
</body>

