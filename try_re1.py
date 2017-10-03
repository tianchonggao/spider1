#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

content='<div class="article block untagged mb15 typs_hot" id="qiushi_tag_119608686">


<div class="author clearfix">
<a href="/users/4745371/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/474/4745371/thumb/4745371.jpg?imageView2/1/w/90/h/90" alt="猪头小小败">
</a>
<a href="/users/4745371/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
猪头小小败
</h2>
</a>
<div class="articleGender womenIcon">31</div>
</div>

<a href="/article/119608686" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


楼主小时候就是调皮捣蛋孩子王<br>平时跟男生爬树打狗<br>有一次跟另外一波孩子打赌<br>输了就当众亲我脚<br>当时我们几个扬眉吐气了几个月。奶奶的，长大后又看到那个亲我脚的小子了，突然觉得小时候真傻x！太特么吃亏了

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1434</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119608686" data-share="/article/119608686" id="c-119608686" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">38</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119608686" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119608686" class="up">
<a href="javascript:voting(119608686,1)" class="voting" data-article="119608686" id="up-119608686" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1462</span>
</a>
</li>
<li id="vote-dn-119608686" class="down">
<a href="javascript:voting(119608686,-1)" class="voting" data-article="119608686" id="dn-119608686" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-28</span>
</a>
</li>
<li class="comments">
<a href="/article/119608686" id="c-119608686" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119608686" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">尼古斯丁.喇兮：</span>
<div class="main-text">
现在亲一下得好几百 可不吃亏了么
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


9

</div>
</div>
</div>
</a>

</div>'

pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?alt="(.*?)"</a><a fref="*?',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0]
