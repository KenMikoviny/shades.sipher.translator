## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/KenMikoviny/shades.sipher.translator/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.


<h1>Test</h1>

<body>
    <input type="text" placeholder="Type something..." id="myInput">
    <button type="button" onclick="getInputValue();">Get Value</button>
    
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
        #'╡': "j",
        "╛": "k",
        "╞": "l",
        '╟': "m",  #not sure
        "╚": "n",
        "╔": "o",
        "╩": "p",
        #"╩": "q",
        "╠": "r",
        '═': "s",
        "╬": "t",
        "╧": "u",
        "╨": "v",
        "╫": "w",
        '╤': "x",
        "╥": "y",
        #"╢": "z",
        " ": " ",
      }
      
        
        function getInputValue(){
            // Selecting the input element and get its value 
            var inputVal = document.getElementById("myInput").value;
            
            // Displaying the value
            alert(inputVal);
        }
    </script>
</body>

