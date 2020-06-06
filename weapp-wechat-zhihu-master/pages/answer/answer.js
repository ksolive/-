//answer.js
var util = require('../../utils/util.js')

var app = getApp()
Page({
  data: {
    motto: '知乎--微信小程序版',
    userInfo: {},
    answerID:-1,
    answerText:''
  },
  //事件处理函数
  toQuestion: function() {
    wx.navigateTo({
      url: '../question/question'
    })
  },
  onLoad: function (options) {    
    this.setData({
    answerID: options.answerID
  });
  console.log(this.data.answerID)
  this.getAnswerText()
        console.log('onLoad')
    var that = this
    //调用应用实例的方法获取全局数据
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })
  },
  tapName: function(event){
    console.log(event)
  },
    getAnswerText:function(){
      var that = this;
      var url = "http://114.55.95.111:10000/answer/getAnswer/"
      wx.request({
        url: url,
        header: { "content-type": "application/x-www-form-urlencoded" },
        method: 'POST',
        data: { id: that.data.answerID },
        success: function (res) {
          console.log(res)
          that.setData({
            answerText: res.data
          })
        }
      })  
    }
})
