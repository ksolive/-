// pages/writer/writer.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    word:'',
    writerID:'',
    open:'',
    title:'test',
    articleID:-1,
    picture:'',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      articleID: options.articleID,
      writerID:getApp().globalData.django_id,
    });
  },

  back:function(){
    wx.navigateBack({
      
    })
  },
  upload:function(e){
    var that = this;
    var user = getApp().globalData.django_id;
    wx.request({
      url: 'http://'+getApp().globalData.serverlocal+'/answer/commitAnswer/',
      header: { "content-type": "application/x-www-form-urlencoded" },
      method: 'POST',
      
      data: {review:that.data.word,articleID:that.data.articleID,writerID:user},
      success: function(res) {
        console.log(res.data)
        wx.navigateBack({})
        wx.showToast({
          title: '评论成功',
          icon: 'success',
          duration: 2000//持续的时间
        })
      }
    })
  },
  input:function(e){
    this.setData({
      word:e.detail.value
    })
  },
  open:function(e){
    this.setData({'open':true})
    this.upload(e);
  },
  ceshi:function(e){
    wx.request({
      url: 'http://'+getApp().globalData.serverlocal+'/test/ceshi/',
      header: { "content-type": "application/x-www-form-urlencoded" },
      method: 'POST',
      success: function(res) {console.log(res.data)}
    })
  }
})