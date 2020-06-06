//logs.js
var util = require('../../utils/util.js')
var app = getApp()
Page({
  data: {
    motto: 'Hello World',
    userInfo: getApp().globalData.username,
    dialogShow: false,
    buttons: [{ text: '取消' }, { text: '确定' }],
    logininf:'',
    unshow:'display:none'
  },
  tryGetInfo:function(){
    
    var that=this;
    
    var userid = app.globalData.django_id;
    
    if(userid != null){
      //转到详情页，包括编辑
      
      wx.navigateTo({
        url: '../me/me',
      })
    }else{
      that.setData({
        dialogShow:true,
        logininf:'还没有注册，要进行注册吗'
      })

    }
  },
  tapDialogButton:function(e){
    var that=this;
    if(e.detail.index!=1){
      this.setData({
        dialogShow:false,
        showOneButtonDialog:false
      });
    }else{
      
      wx.navigateTo({
        url: '../test/test',
        success: (result) => {that.setData({
          dialogShow:false
        })},
      })
    }
  },
  helps:function(e){

  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: ''
    })
  },
  onLoad: function () {
    console.log('onLoad')
    var that = this
    //调用应用实例的方法获取全局数据
    if(app.globalData.userPower>=1){
      that.setData({
        unshow:'',
        userInfo: getApp().globalData.username
      })
    }
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })
  },
  MyArticle: function(){
    wx.navigateTo({
      url: '../Myarticlelist/Myarticlelist'
    })
  },
  onShow:function(){
    var that = this;
    that.setData({
      userInfo:getApp().globalData.username
    })
  }
})

