# Vue 3 学习笔记

## 第一节 学习资料

https://github.com/komavideo/LearnVue3

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
> 4. 绑定不再是div属性 是Vue数据

## 第六节  v-if

> 控制元素显示条件

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <p>
            <button class="btn btn-success" v-on:click="this.seen = !this.seen">设定按钮</button>
        </p>
        <div v-if="seen">能看见我吗？</div>
    </div>
    <script>
        const HelloVueApp = {
            data() {
                return {
                    seen: true
                }
            },
        }
        Vue.createApp(HelloVueApp).mount('#hello-vue')
    </script>
</body>
~~~



> 1. v-on 绑定click，可以改变seen这个变量的值，取反操作
> 2. div 中增加 v-if 属性并关联变量seen
> 3. 可以控制DOM树在源代码的整个显示与消失

## 第七节 v-for 循环

> v-for循环一个数组

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <button class="btn btn-success" v-on:click="this.seen = !this.seen">今天的预定</button>
        <hr>
        <ol>
            <li v-for="todo in todos" v-if="seen">
                {{ todo.text }}
            </li>
        </ol>
    </div>
    <script>
        const HelloVueApp = {
            data() {
                return {
                    seen: false,
                    todos: [
                        { text: '吃饭' },
                        { text: '睡觉' },
                        { text: '打游戏' }
                    ]
                }
            },
        }
        Vue.createApp(HelloVueApp).mount('#hello-vue')
    </script>
</body>
~~~



> 1. 实际开发中，数组一般来自后端，通过API等得出，比如新闻列表；员工列表
> 2. data函数定义了seen和todos
> 3. todos是一个数组，可以迭代循环
> 4. v-for 和 v-if 类似，使用上看做div的一个属性
> 5. Vue 2 使用方法一样

## 第八节 自定义组件 component

> 大部分工作内容是开发小组件，组合达到目的

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <!-- 取反按钮-->
        <button class="btn btn-success" v-on:click="this.seen = !this.seen">万能按钮</button>
        <hr>
        <!-- 引入小组件-->
        <hello-world myname="koma" v-if="this.seen" />        
    </div>
    <script>
        //声明app 组件对象 HelloVueApp，只提供一个数据seen
        const HelloVueApp = {
            data() {
                return {
                    seen: true,
                }
            },
        }
        //实例化Vue整个应用给app
        const app = Vue.createApp(HelloVueApp)
        //在app里调用component方法，在app增加一个组件 hello-world
        app.component('hello-world', {
            //描述组件的细节，接受myname属性
            props: ['myname'],
            //呈现的html模板
            template: `<h1>hello {{ myname }}.</h1>`
        })
        //app绑定到div
        app.mount('#hello-vue')
    </script>
</body>
~~~

> 1. <hello-world myname="koma" v-if="this.seen" />  
>
>    产生的是模板<h1>里的内容
>
> 2. 因为hello-world 不是一个有效的div 名称，而是调用app的component
>
> 3. 注册组件后，组件接受属性 myname ，myname 在 调用是给出。property 属性

## 第九课 对象实例

> 实例的生产和使用

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <!-- 数据模板的值 -->
        {{ a }}
    </div>
    <script>
        // 定义自己的数据对象
        const myData = { a: 10 } //初始赋值为10
        const vm = Vue.createApp({//实例化静态函数/* options */
            data() {
                // App返回自定义的数据对象
                return myData  //返回上方的定义好的myData
            }
        }).mount('#hello-vue')
        // 打印数据
        console.log(vm.a)	// vm 里a的值
        console.log(vm.$data) //数据对象的值，是一个代理，代理有Object
        console.log(myData)	//是Object
        // 改变数据的值
        vm.a = 100
        console.log(vm.a)
        console.log(vm.$data) // Vue实例属性
        console.log(myData)
    </script>
</body>
~~~

> 1. 指针引用，不是值的拷贝
> 2. 对象值改变，是双向的

##  CLI 命令行工具包

> 使用Vue命令行工具创建Vue 3 工程

~~~ssh
sudo npm install -g @vue/cli@next 
vue -V //4.5以上
vue create hello-vues
~~~

## 第十节 生命周期

>1. 每个实例创建都会经历初始化的一系列步骤
>2. 钩子函数，在特定阶段添加自定义代码
>3. 官网生命周期API : https://v3.vuejs.org/api/options-lifecycle-hooks.html
>4. 小马Vue模板工具包 http://tools.komavideo.com/#/home/code-template

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        {{ x + y }} <!-- 页面输出计算结果 -->
    </div>
    <script>
        Vue.createApp({/* options */
            data() {
                return {
                    x: 10,
                    y: 20,
                }
            },
            created() {
                // 组件生成时，在F12命令行里输出日志
                console.log('x + y is: ' + (this.x + this.y))
            }
        }).mount('#hello-vue')
    </script>
</body>
~~~

> beforeCreate: function() {},
> created: function() {},
> beforeMount: function() {},
> mounted: function() {},
> beforeUpdate: function() {},
> updated: function() {},
> activated: function() {},
> deactivated: function() {},
> beforeDestroy: function() {},
> destroyed: function() {
> },
> errorCaptured: function() {}

## 第十一节  插值 语法v-once,v-html,v-bind

>  

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <h3>插值语法</h3>
        <span class="text-primary">{{ message }} </span> //text-primary 蓝色字体

        <hr>
        <h3>只渲染一次 - v-once</h3>
        <span v-once class="text-danger">{{ message }}</span>
        <br>
        <button class="btn btn-info" v-on:click="this.message='不要太悲观, 虽然上帝看不到。'">哦？</button> //点击改变message内容
        
        <hr>
        <h3>原始HTML - v-html</h3>
        {{ rawHtml }} //原始HTML
        <br>
        <span v-html="rawHtml"></span> //转化刷出，存在安全隐患
        
        <hr>
        <h3>绑定属性 - v-bind:xxx</h3>
        <button v-bind:disabled="isDisabledButton" v-on:click="this.isDisabledButton=true" class="btn btn-info">按我一下吧</button>
    </div>
    <script>
        Vue.createApp({/* options */
            data() {
                return {
                    message: '中国足球没戏了!',
                    rawHtml: '<b class=text-danger>恒大衰落了</b>',
                    isDisabledButton: false
                }
            },
        }).mount('#hello-vue')
    </script>
</body>
~~~

> 1. 胡子（插值）语法为何可以显示正确的值，
>    * id 绑定给Vue内部核心
> 2. bootstrap 语法，text-primary 蓝色字体
> 3. v-once 如果代码值变化，不会再次渲染，不会双向变化。不用赋值，就是一个属性
> 4. 原始客户输入代码，直接v-html使用有安全风险需要白名单处理
> 5. button的disable属性是HTML5原生的

## 第十二节  简化 v-bind 和 v-on

> * v-bind 绑定属性 -> :attr
> * v-on 绑定事件 -> @event

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <h3>属性绑定</h3>
        <!-- 完整写法：v-bind:href -->
        <a v-bind:href="komavideo" class="link" target="_blank">小马视频</a><br />
        <!-- 省略写法：:href -->
        <a :href="komavideo" class="link" target="_blank">小马视频</a>
        <h3>事件绑定</h3>
        <!-- 完整写法：v-on:click -->
        <button v-on:click="buyPS5(1)" class="btn btn-success">买PS5</button>
        <!-- 省略写法：:href -->
        <button @click="buyPS5(0)" class="btn btn-danger">不买PS5</button>
    </div>
    <script>
        Vue.createApp({/* options */
            data() {
                return {
                    komavideo: 'http://komavideo.com'
                }
            },
            methods: {
                buyPS5(val) {
                    val == 1 ? alert("买买买！！！") : alert("不买不买不买！！！")
                }
            }
        }).mount('#hello-vue')
    </script>
</body>
~~~

1. buyPS5 就是一个methods里的函数，接受参数传入
2. 减少代码量
3. methods是关键词，不可改变

## 第十三节 getter 计算属性

> Vue 2 /3 ,Angular 都有存在，统计其他变量,取得计算属性

~~~html
 <div id="hello-vue" class="m-3 p-3 border border-success">
        <h3>我今年通关了这几个游戏：</h3>
        <ol>
            <li v-for="game in games">{{ game }}</li>
        </ol>
        <hr>
        <div class="lead">
            数数看，我今年一共通关了 <b class="text-danger">{{playedGameCount}}</b> 款游戏。
        </div>
    </div>
    <script>
        Vue.createApp({/* options */
            data() {
                return {
                    games: [
                        "纸片马里奥",
                        "勇者斗恶龙建造者2",
                        "赛博朋克2077",
                        "BrawlStars",
                    ]
                }
            },
            computed: {
                playedGameCount() {
                    return this.games.length
                }
            }
        }).mount('#hello-vue')
    </script>
~~~

1. 使用v-for 循环输出 li 
2. this.games.length 不会去重
3. 列表最后一个逗号，可有可无
4. playedGameCount 是函数

## 第十四节 setter 计算属性

> 设置计算属性

~~~html
 <div id="hello-vue" class="m-3 p-3 border border-success">
        <h3>{{this.x}} + {{this.y}} = {{this.result}}</h3>
        <button @click="this.result=100" class="btn btn-success">重新设定 x, y</button>
    </div>
    <script>
        Vue.createApp({/* options */
            data() {
                return {
                    x: 10,
                    y: 20,
                }
            },
            computed: {
                result: {
                    // getter
                    get() {
                        return this.x + this.y
                    },
                    // setter
                    set(newValue) {
                        this.x = newValue - 30
                        this.y = 30
                    }
                }
            }
        }).mount('#hello-vue')
    </script>
~~~

1. 提供X Y 两个属性
2. 动态改变XY的值，不要改变计算属性，设为只读函数
3. @click 中对result进行的修改
4. z = Math.ceil(Math.random()*100)
5. 可以读值和写值

## 第十五节 计算属性与函数区别

>计算属性，可以读写值。函数也可以。

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <h2>{{ msg }} / {{ this.getResult() }}</h2>
        <h3>result: {{this.result}} / {{ this.getDateTime() }}</h3>
        <button @click="btnClick()" class="btn btn-success">一个按钮</button>
    </div>
    <script>
        Vue.createApp({
            /* options */
            data() {
                return {
                    msg: "i love u." //数据对象
                }
            },
            computed: {
                result() {	//计算属性
                    // return this.msg
                    return this.getDateTime() //计算属性调用函数，获取系统时间
                }
            },
            methods: {//函数部分
                getResult() {
                    return this.msg
                },
                getDateTime() {
                    now = new Date()
                    return "00:" + now.getMinutes() + ":" + now.getSeconds()
                },//分秒时间，函数获取时间
                btnClick() {
                    console.log("this.result:", this.result)//计算属性，不会变化，缓存cache
                    console.log("this.getDateTime():", this.getDateTime())//调用函数，新的时间对象
                }
            }
        }).mount('#hello-vue')
    </script>
</body>
~~~

1. methods 函数每次执行，产生新的对象。
2. computed 计算属性是被缓存的
3. 尽可能不依赖计算属性，进行业务逻辑计算。仅做辅助显示。

## 第十六节 watch

>观察者属性使用方法
>
>侦测页面绑定数据的更改

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <p>
            有什么问题吗:
            <input v-model="question" /><!-- 数据绑定文本框 -->
        </p>
        <p>
            {{ msg }}
            <hr>
            <img :src="answer" alt=""> <!-- 显示图片-->
        </p>
    </div>
    <script>
        Vue.createApp({
            /* options */
            data() {
                return {//三个数据值
                    question: '',
                    answer: '',
                    msg: "",//提示信息
                }
            },
            watch: {//观察属性
                question(newQuestion, oldQuestion) {//观察question
                    if (newQuestion.indexOf('?') > -1) {//用户输入有无问号
                        this.getAnswer() //返回答案
                    } else {
                        this.msg = ""
                        this.answer = ""
                    }
                }
            },
            methods: {
                getAnswer() {
                    this.msg = "考虑中..."
                    axios//库，script中有引用
                        .get('https://yesno.wtf/api')
                        .then(response => {
                            this.msg = response.data.answer
                            this.answer = response.data.image
                        })
                        .catch(error => {
                            this.msg = 'Error! Could not reach the API. ' + error
                        })
                }
            }
        }).mount('#hello-vue')
    </script>
    <script src="https://cdn.jsdelivr.net/npm/axios@0.12.0/dist/axios.min.js"></script>
</body>
~~~

1. https://yesno.wtf/api 返回jason

   ~~~json
   {"answer":"yes","forced":false,"image":"https://yesno.wtf/assets/yes/9-6403270cf95723ae4664274db51f1fd4.gif"}
   ~~~


## 第十七节 动态样式单绑定

> 组建中绑定css样式单

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <div class="text-danger border display-5">我爱NBA!</div><!--dispaly 5 字体--></！--dispaly>
        <hr>
        <div :class="{ 'text-danger': isLoveCBA, border: isLoveCBA, 'display-5': isLoveCBA }">我爱CBA!</div>
    <!--冒号v-bind属性绑定class，判断bootstrap5的属性是不是true -->
        <button @click="this.isLoveCBA=!this.isLoveCBA" class="btn btn-info">爱CBA</button>
    <!--v-on事件绑定，按钮改变 isLoveCBA值-->
        <hr>
        <div :class="cssCUBA">我爱CUBA!</div>
    <!-- 绑定cssCUBA 对象，-->
        <button @click="this.cssCUBA=this.cssTitle" class="btn btn-info">爱CUBA</button>
    <!--把cssTitle 赋值给cssCUBA，改变样式。成为CSS样式绑定 -->
        <hr>
        <!-- 直接绑定style属性, 不用class方式 -->
        <div :style="cssWNBA">我爱WNBA!</div>
    <!--:style,不用定义css class -->
    </div>
    <script>
        Vue.createApp({
            /* options */
            data() {
                return {//数据内容
                    isLoveCBA: false, //布尔型
                    cssCUBA: {},	//json 型，可以给初始值
                    cssTitle: {//bootstrap中css定义的class
                        'text-danger': true,
                        'border': true,
                        'display-5': true,
                    },
                    cssWNBA: {//Dhtml
                        color: 'pink',
                        fontSize: '36px'
                    }
                }
            },
            methods: {}
        }).mount('#hello-vue')
    </script>
</body>
~~~

1. 三种方式绑定css样式

   * 写好对应的样式，然后true false绑定变量

   * 绑定:class 到某个json型变量

     ~~~html
     <div class="text-danger border display-5">
     ~~~

     

   * 直接绑定:style ，不用再指定class 

     ~~~html
     <div style="color: pink; font-size: 36px;">
     ~~~



## 第十八节 条件渲染

> 根据条件值，是否渲染html内容
>
> v-if / v-else-if / v-else

~~~html
<body>
    <div id="hello-vue" class="m-3 p-3 border border-success">
        <div v-if="isLoveGame" class="display-5 text-primary">一定要买 PS5.</div>
        <!--判断是否为真 -->
        <div v-else class="display-5 text-success">好好学习，天天向上。</div>
        <hr>
        <template v-if="isLoveGame">
            <!--template是HTML5中脚本-->
            <h3>必买游戏</h3>
            <ol>
                <li>塞伯朋克2077</li>
                <li>文明7</li>
                <li>街头霸王6</li>
            </ol>
        </template>
        <hr>
        <div v-if="this.playedYears >= 10" class="display-5">资深玩家</div>
        <div v-else-if="this.playedYears >= 5" class="display-5">老玩家</div>
        <div v-else-if="this.playedYears >= 2" class="display-5">入门级</div>
        <div v-else class="display-5">菜鸟一枚</div>
    </div>
    <script>
        Vue.createApp({
            /* options */
            data() {
                return {//两个布尔值
                    isLoveGame: true,
                    playedYears: 10,
                }
            },
            methods: {}
        }).mount('#hello-vue')
    </script>
</body>
~~~

1. 只会显示符合判断的div