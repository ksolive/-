//answer.js
var util = require('../../utils/util.js')

var app = getApp()
Page({
  data: {
    motto: '知乎--微信小程序版',
    userInfo: {},
    id:'',
    result:'',
    answerList:''
  },
  //事件处理函数
  towriter:function(){
    wx.navigateTo({
      url: '../reviewWriter/reviewWriter?articleID='+this.data.id,
    })
  },
  bindItemTap: function(e) {
    var answerid = e.currentTarget.dataset.id
    wx.navigateTo({
      url: '../answer/answer?answerID='+answerid
    })
  },
  onLoad: function (options) {
    
    console.log(options.id)
    var that = this
    that.setData({
      id:options.id
    })
    console.log(this.data.id)
    this.getd()
        //调用应用实例的方法获取全局数据
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })
    this.getAnswerList()
  },
  getd: function(){
    var that = this;
    var url="http://"+getApp().globalData.serverlocal+"/article/article_detail/"+that.data.id; //结合登入后，后台验证是否获得私密发布，request.user.id
    wx.request({
      url: url,
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        console.log(res.data)
        console.log(res)
        console.log(typeof(res.data))
        that.setData({
          result:res.data[0]
        })
      }
    })
  },
  tapName: function(event){
    console.log(event)
  },
  onShow: function(){
    this.getAnswerList()
  },
  getAnswerList:function(){
    var that = this;
    var url = "http://"+getApp().globalData.serverlocal+"/answer/getAnswerList/"
    wx.request({
      url: url,
      header: { "content-type": "application/x-www-form-urlencoded" },
      method:'POST',
      data:{id:that.data.id},
      success: function (res) {
        console.log(res.data)
        that.setData({
          answerList: res.data
        })
      }
    })
  }

})
