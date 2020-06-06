//index.js

var util = require('../../utils/util.js')
var app = getApp()
Page({
  data: {
    navTab: ["推荐"],
    currentNavtab: "0",
    imgUrls: [
      '../../images/swiper-1.jpg',
      '../../images/swiper-2.jpeg',
      '../../images/swiper-3.jpeg'
    ],
    indicatorDots: false,
    autoplay: true,
    interval: 5000,
    duration: 1000,
    feed: [],
    result:'',
    feed_length: 0
  },
  //事件处理函数
  adddetial: function() {
    wx.navigateTo({
      url: '../writer/writer',
    })
  },
  bindItemTap: function(e) {
    wx.navigateTo({
      url: '../answer/answer'
    })
  },
  bindQueTap: function(e) {
    var i=e.currentTarget.dataset.id
    wx.navigateTo({
      url: '../question/question?id='+i
    })
  },
  onLoad: function () {
    console.log('onLoad')
    var that = this
    //调用应用实例的方法获取全局数据
    this.getd();
  },
  upper: function () {
    wx.showNavigationBarLoading()
    this.getd();
    this.refresh();
    console.log("upper");
    setTimeout(function(){wx.hideNavigationBarLoading();wx.stopPullDownRefresh();}, 2000);
  },
  lower: function (e) {
    wx.showNavigationBarLoading();
    var that = this;
    this.getd();
    setTimeout(function(){wx.hideNavigationBarLoading();that.nextLoad();}, 1000);
    console.log("lower")
  },
  //scroll: function (e) {
  //  console.log("scroll")
  //},

  //网络请求数据, 实现首页刷新
  refresh0: function(){
    var index_api = '';
    this.getd();
    util.getData(index_api)
        .then(function(data){
          //this.setData({
          //
          //});
          console.log(data);
        });
  },

  //使用本地 fake 数据实现刷新效果
  getData: function(){
    var feed = util.getData2();
    this.getd();
    console.log("loaddata");
    var feed_data = feed.data;
    this.setData({
      feed:feed_data,
      feed_length: feed_data.length
    });
  },
  getd: function(){
    var that = this;
    wx.request({
      url: 'http://'+getApp().globalData.serverlocal+'/article/article_list/',
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        console.log(res.data)
        console.log(res)
        console.log(typeof(res.data))
        that.setData({
          result:res.data
        })
      }
    })
  },
  refresh: function(){
    wx.showToast({
      title: '刷新中',
      icon: 'loading',
      duration: 2000
    });
    var feed = this.getd();
    console.log("loaddata");
    setTimeout(function(){
      wx.showToast({
        title: '刷新成功',
        icon: 'success',
        duration: 500
      })
    },3000)

  },

  //使用本地 fake 数据实现继续加载效果
  nextLoad: function(){
    this.getData()
    wx.showToast({
      title: '加载中',
      icon: 'loading',
      duration: 4000
    })
    var next = util.getNext();
    console.log("continueload");
    var next_data = next.data;
    this.setData({
      feed: this.data.feed.concat(next_data),
      feed_length: this.data.feed_length + next_data.length
    });
    setTimeout(function(){
      wx.showToast({
        title: '加载成功',
        icon: 'success',
        duration: 2000
      })
    },3000)
  },
  onShow: function () {
    this.refresh();
  },
})
