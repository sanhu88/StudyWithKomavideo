# Vue 3 学习笔记

## 第一节 引入

入门教程，小马老师使用的是css样式引入，而且还同时加入了Bootstrap

~~~html
<!--引用Vue 最新版	-->
<script src="https://unpkg.com/vue@next"></script>
	
<!--引入bootstrap  -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">
~~~

index.html 代码

~~~html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue 3.0 - 小马技术</title>
	
	<!--引用Vue 最新版	-->
    <script src="https://unpkg.com/vue@next"></script>
	
	<!--引入bootstrap  -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous"> 
</head>
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
	<!-- m-3 p-3 border border-success 为bootstrap的样式-->
        {{ message }}
    </div>
	
    <script>
        const HelloVueApp = {
            data() {
                return {
                    message: 'Hello Vue!!'
                }
            }
        }
        Vue.createApp(HelloVueApp).mount('#hello-vue') //创建后挂载（绑定）到ID
    </script>    
</body>
</html>
~~~

