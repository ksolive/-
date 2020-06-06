// pages/Myarticlelist/Myarticlelist.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    result:'',
    id:'',
    showButtonDialog1:false,
    buttons: [{ text: '取消' }, { text: '确定' }],
    oneButton: [{ text: '返回' }],
  },
  showdialog1: function(e){
    this.setData({
      showButtonDialog1:true,
      id:e.currentTarget.dataset.id,
    })
  },
  displaydialog: function(){
    this.setData({
      showButtonDialog1:false,
    })
  },
  trigger: function(e){
    var that=this
    if (e.detail.index==1){
      this.article_delete()
      setTimeout(function(){that.getd()},100)
      this.displaydialog()

    }
    else{
      this.displaydialog();
    }
  },
  getd: function(){
    var that = this;
    var user = getApp().globalData.django_id;
    wx.request({
      url: 'http://'+getApp().globalData.serverlocal+'/article/article_Mylist/',
      header: { "content-type": "application/x-www-form-urlencoded" },
      data:{
        user:user
      },
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
  article_delete: function(e){
    var that = this;
    console.log(this.data.id)
    var url="http://"+getApp().globalData.serverlocal+"/article/article_delete/"+that.data.id;
    
    wx.request({
      url: url,
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        console.log(res.data)
        console.log(res)
        console.log(typeof(res.data))
      }
    })
  },
  article_update: function(e){
    var i=e.currentTarget.dataset.id
    console.log(i)
    wx.navigateTo({
      url: '../writer/writer?id='+i,
    })
  },
  refresh: function(){
    wx.showToast({
      title: '刷新中',
      icon: 'loading',
      duration: 2000
    });
    this.getd();
    console.log("loaddata");
   
    setTimeout(function(){
      wx.showToast({
        title: '刷新成功',
        icon: 'success',
        duration: 2000
      })
    },3000)

  },
  bindQueTap: function(e) {
    var i=e.currentTarget.dataset.id
    wx.navigateTo({
      url: '../question/question?id='+i
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getd();
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
    this.getd();
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