// pages/mechange/mechange.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userinfo:{
      name:'',
      sex:'',
      hobit:'',
      age:'',
      password:''
  }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  name:function(e){
    var that=this;
    that.setData({
      user:e.detail.value
    })
  },
  sex:function(e){
    var that=this;
    that.setData({
    })
  },
  age:function(e){
    var that=this;
    that.setData({
      user:e.detail.value
    })
  },
  hobit:function(e){
    var that=this;
    that.setData({
      user:e.detail.value
    })
  },
  password:function(e){
    var that=this;
    that.setData({
      user:e.detail.value
    })
  },
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})