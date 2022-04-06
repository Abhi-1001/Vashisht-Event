# LangWars

**Let's design with code!**

You are supposed to recreate the StyleSheet only given an image. You get a points based on how much your output matches with the target and bonus if it is achieved with the lesser code in comparison.

---

# List of Target Images

Try to complete as many images as possible in the given time.

- [#1](./files/1.md)
- [#2](./files/2.md)
- [#3](./files/3.md)
- [#4](./files/4.md)
- [#5](./files/5.md)
- [#6](./files/6.md)
- [#7](./files/7.md)
- [#8](./files/8.md)
- [#9](./files/9.md)
- [#10](./files/10.md)
- [#11](./files/11.md)
- [#12](./files/12.md)
- [#13](./files/13.md)
- [#14](./files/14.md)
- [#15](./files/15.md)
- [#16](./files/16.md)
- [#17](./files/17.md)
- [#18](./files/18.md)
- [#19](./files/19.md)
- [#20](./files/20.md)
- [#21](./files/21.md)
- [#22](./files/22.md)
- [#23](./files/23.md)
- [#24](./files/24.md)
- [#25](./files/25.md)
- [#26](./files/26.md)
- [#27](./files/27.md)
- [#28](./files/28.md)
- [#29](./files/29.md)
- [#30](./files/30.md)
- [#31](./files/31.md)
- [#32](./files/32.md)
- [#33](./files/33.md)
- [#34](./files/34.md)
- [#35](./files/35.md)
- [#36](./files/36.md)
- [#37](./files/37.md)
- [#38](./files/38.md)
- [#39](./files/38.md)
- [#40](./files/40.md)
- [#41](./files/41.md)
- [#42](./files/42.md)

---

# How to submit

Type your code only inside the `body` tag.

For Example -

```html
<!-- Type your code inside here -->
<body>
    <div></div>
    <style>
        * {
            margin: 0;
        }
        body {
            background: #5d3a3a;
            height: 298px;
            width: 398px;
        }
        div {
            width: 200px;
            height: 200px;
            background: #b5e0ba;
        }
    </style>
</body>
```

Save the `index.html` as `index{id}.html`.

For Example - If your **Id** is **34**, then save your file as `index34.html`.

### DO NOT edit anything outside of the `body` tag.

### DO NOT create another file, make all the changes inside the same `index.html` file.

---

# Code for getting the Output Image from `index.html` file

Put all the index.html files into a single folder. In the python file, go to line number 38 and replace the `input_path` variable with path to your folder that has all the `index.html` files

```python
input_path = "D:/my_folder/subfolder"
```

For running the python code, open your `cmd` terminal,
- Run `pip install -r requirements.txt`
- Then run `python Tester.py`

This will generate all the output images for you, from the `index.html` files.

The output for `index13.html` will be `out13.png`.

---

# How to use Image Slider

Modify the image path in the `img` tag  by editing the `src` element. Add the path to both the original image and your modified image in

```html
<img src="D:/my_folder/some_sub_folder/1.png" alt="Original Image">
<span class="cd-image-label" data-type="original">Original</span>

<div class="cd-resize-img"> <!-- the resizable image on top -->
    <img src="D:/my_folder/some_sub_folder/out1.png" alt="Modified Image">
    <span class="cd-image-label" data-type="modified">Modified</span>
</div>
```

You can slide and check the images to see whether both are matching.

---

## Submission Link - https://forms.gle/uhjd6W3WxrSPaFMK6
