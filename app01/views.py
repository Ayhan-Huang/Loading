from django.shortcuts import render
from django.http import JsonResponse
from django.utils.safestring import mark_safe


def test(request):
    return render(request, 'test.html')


def ajax_handler(request):
    # 模拟网络延迟
    import time
    time.sleep(3)

    msg = '''<p>我们通常将JS代码写在一个单独的JS文件中，然后在页面中引入该文件。但是，有时候引入后会碰到变量名或函数名与其它JS代码冲突的问题。那么如何解决这个问题呢？作用域隔离。在JS中，作用域是通过函数来划分的，将JS代码封装到函数中进行调用可以避免变量名/函数名冲突的问题，但是这也并不是万无一失，因为封装函数本身有可能和其它函数重名，解决方案：自执行函数。</p>

<p>自执行函数是用一对圆括号将匿名函数包起来，加括号（传参）会立即执行。因为函数无名字，实现了作用域的绝对隔离和函数名的冲突问题。基本形式如下：</p>

<pre class="prettyprint"><code class="language-javascript hljs ">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-params">()</span> {</span>
    console.log(<span class="hljs-string">'do something'</span>);
})();</code></pre>

<p><br></p>

<p>比如我们在custome.js文件中写了一些JS逻辑，并封装到函数<code>init</code>中。我们用自执行函数将自己定义的函数<code>init</code>包起来，就像下面这样。</p>



<pre class="prettyprint"><code class="language-javascript hljs ">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-params">()</span> {</span>

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span><span class="hljs-params">()</span> {</span>
        console.log(<span class="hljs-string">'execute init...'</span>);
    }

    init();
})();</code></pre>

<p>当我们在html中引入custome.js：<code>&lt;script src="custome.js"&gt;&lt;/script&gt;</code>，自执行函数会立即执行，进而执行内部定义的<code>init</code>函数：</p>
'''

    return JsonResponse({"content": mark_safe(msg)})
