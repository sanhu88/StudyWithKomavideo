# Vue 3 学习笔记

## 第二节 引入

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

## 第三节 v-bind 数据绑定

~~~html
	<div id="hello-vue" class="m-3 p-3 border border-success">
	<!-- m-3 p-3 border border-success 为bootstrap的样式-->
        <div v-bind:title="message">
            走开，别把鼠标放上来。
        </div>
    </div>

	<script>
        const HelloVueApp = {
            //数据提供函数
			data() {
                return {
                    message: 'Get Away!'
                }
            }
        }
        Vue.createApp(HelloVueApp).mount('#hello-vue') //创建后挂载（绑定）到ID
    </script>   
~~~

> 数据绑定，把关键词，写在 div属性的前面，其他和普通div一致
>
> 其中message ，可以替换成其他名称
>
> 其中v-bind: 可以缩写 :

## 第四节 v-on 事件处理

> 使用v-on绑定一个click事件

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <h3>{{ message }}</h3>
        <button class="btn btn-success" v-on:click="reverseMessage">反转字符串</button>
    </div>
    <script>
        const HelloVueApp = {
            data() {
                return {
                    message: '上海自来水来自海上，黄山落叶松叶落山黄'
                }
            },
            methods: {
                reverseMessage() {
                    //定义函数
                    this.message = this.message
                        .split('')
                        .reverse()
                        .join('')
                }
            }
        }
        Vue.createApp(HelloVueApp).mount('#hello-vue')
    </script>    
</body>
~~~

> 1. Vue 2 就有v-on 了
> 2. 可以绑定其他鼠标操作

## 第五节 v-model

> 变量双向绑定

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <p>{{ message }}</p>
        <input class="form-control" v-model="message" />
    </div>
    <script>
        const HelloVueApp = {
            data() {
                return {
                    message: 'v-model 双向绑定'
                }
            },
        }
        Vue.createApp(HelloVueApp).mount('#hello-vue')
    </script>    
</body>
~~~

> 1. 文本会同时显示在input文本框中
> 2. 修稿了input内容，p段落也会改变。
> 3. 联想到，银行卡卡号输入时，放大显示核对