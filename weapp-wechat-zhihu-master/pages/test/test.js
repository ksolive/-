// pages/test/test.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    user:'',
    pass:'',
    dialogShow: false,
    showOneButtonDialog:false,
    oneButton: [{ text: '确定' }],
    buttons: [{ text: '取消' }, { text: '确定' }],
    logininf:''
  },
  tran:function(e){
    console.log(1);
    wx.navigateTo({
      url: '../writer/writer',
    })
  },
  
  user:function(e){
    var that=this;
    that.setData({
      user:e.detail.value
    })
  },
  pass: function (e) {
    var that = this;
    that.setData({
      pass:e.detail.value
    })
  },
  login:function(e){
    var that=this;
    wx.request({
      url: 'http://'+getApp().globalData.serverlocal+'/test/login/',
      header: {
        "content-type": "application/x-www-form-urlencoded"
      },
      data: {user:this.data.user,psd:this.data.pass},
      method: 'POST',

      success: function(res) {
        var app=getApp();
        console.log(res.data)
        app.globalData.django_id=res.data.id;
        app.globalData.cookie=res.data.cookie;
        //app.globalData.userPower=res.data;
        if(app.globalData.django_id>=0){
          that.setData({
            showOneButtonDialog:true,
            logininf:'登录成功',        
          });
          console.log(app.globalData.django_id);
          getApp().globalData.username=that.data.user
        }else if(res.data==-2){
          that.setData({
            dialogShow:true,
            logininf:'该用户名还没有注册，要注册吗'
          })
          console.log(app.globalData.django_id);
        }else if(res.data==-3){
          that.setData({
            dialogShow:true,
            logininf:'用户名和密码有非法字符，仅支持字母数字与下划线'
          })
        }else if(app.globalData.django_id==-1){
          that.setData({
            logininf:'该用户已注册且您输入的密码错误，请检查密码登录，或更换用户名注册',
            dialogShow:true
          })
        }
      },
      
      fail: function(res) {
        that.setData({
          showOneButtonDialog: true,
          logininf: '出现了一些问题'
        });
      },
    })
  },
  tapDialogButton:function(e){
    if(e.detail.index!=1){
      this.setData({
        dialogShow:false,
        showOneButtonDialog:false
      });
      wx.navigateBack({
        delta:1
      })
    }else{
      console.log(this.data);
      var that=this;
      wx.request({
        url: 'http://'+getApp().globalData.serverlocal+'/test/signup/',
        header: {
          "content-type": "application/x-www-form-urlencoded"
        },
        data:{user:that.data.user,psd:that.data.pass},
        method: 'POST',
        success: function(res) {
          getApp().globalData.django_id=res.data.id;
          getApp().globalData.cookie=res.data.cookie;
          that.setData({
            dialogShow:false,showOneButtonDialog:true,logininf:'注册成功并以登陆'
          })
        },
        fail: function(res) {console.log(22)},
      })
    }
  },
  logout:function(e){
    var that=this;
    wx.request({
      url: 'http://'+getApp().globalData.serverlocal+'/test/logout/',
      header: { "content-type": "application/x-www-form-urlencoded"},
      method: 'POST',
      success: function(res) {
        that.setData({
          showOneButtonDialog:true,
          logininf:'登出成功'
        })
        console.log(res.data);
      }
    })
  },
 

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})