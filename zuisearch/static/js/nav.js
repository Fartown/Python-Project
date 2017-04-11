var detail = document.getElementsByClassName('detail');
var navList = document.getElementsByClassName("nav_list");
var dotList = document.getElementsByClassName('dot');
var content = document.getElementsByClassName('content')[0];
detail[0].className = detail[0].className + ' ' + 'detail_active';
dotList[0].className = dotList[0].className + ' ' + 'dot_active';
// 导航切换事件处理
for (var i = detail.length - 1; i >= 0; i--) {
    (function(i) {
        navList[i].onclick = function() {
            for (var j = navList.length - 1; j >= 0; j--) {
                (function(j) {
                    detail[j].className = 'detail';
                    dotList[j].className = 'dot';
                })(j)
            }
            detail[i].className = detail[i].className + ' ' + 'detail_active';
            dotList[i].className = dotList[i].className + ' ' + 'dot_active';
        }
    })(i)
}
// 轮播事件处理
var num = 0;
addEvent(content, "mousewheel", function(event) {
    var detailActive = document.getElementsByClassName('detail_active')[0];
    var liList = document.getElementsByClassName('dot_active')[0].getElementsByTagName('li');
    var itemList = detailActive.getElementsByClassName('item'); 
    var count = Math.floor(itemList.length / 16);
    console.log(count+'/'+itemList[0]);
    var width = (itemList[0].offsetWidth + itemList[0].offsetLeft) * 4;
    if (event.delta < 0 && num < count) {
        num++;
        detailActive.style.left = -num * (itemList[0].offsetWidth + itemList[0].offsetLeft) * 4 + 'px';
        for (var i = 0; i < liList.length; i++) {
            liList[i].className = '';
        }
        liList[num].className = 'li_focus';
    }
    if (event.delta > 0 && num > 0) {
        num--;
        detailActive.style.left = -num * width + 'px';
        for (var i = 0; i < liList.length; i++) {
            liList[i].className = '';
        }
        liList[num].className = 'li_focus';
    }
});
