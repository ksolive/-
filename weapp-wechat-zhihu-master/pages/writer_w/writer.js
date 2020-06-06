// pages/writer/writer.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    author:'',
    title:'',
    body:'',
    picture:'',
    privacy:'',
    username:'cc',
    password:'13799959688q',
    result:'',
    showOneButtonDialog1:false,
    showOneButtonDialog2:false,
    showOneButtonDialog3:false,
    oneButton: [{ text: '返回' }],
    texttt:'hhhhhh',
    article_id:'',
    //buttons: [{ text: '取消' }, { text: '确定' }],
  },

  /**
   * 生命周期函数--监听页面加载
   */

  onLoad: function (options) {
    console.log(options)
    var that = this
    that.setData({
      article_id:options.id
    })
    console.log(this.data.article_id)
    if(this.data.article_id!=undefined){
      this.get_detail()
    }
    //this.getd()
    //调用应用实例的方法获取全局数据
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

  },
  back:function(){
    wx.navigateBack({
    })
  },
  upload_open:function(e){
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:8000/article/article_create/',
      header: { "content-type": "application/x-www-form-urlencoded" },
      method: 'POST',
      data: {
        title:that.data.title,
        body:that.data.body,
        picture:that.data.picture,
        privacy:'0',
        
      },
      success: function(res) {
        //console.log(res.data)
        if(res.data!='表单内容有误，请重新填写。'){
        that.setData({
          showOneButtonDialog1:true
        });
        }
        else{
          that.setData({
            showOneButtonDialog2:true
          });
          
        }
      }
    })
    
  },
  upload_privacy:function(e){
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:8000/article/article_create/',
      header: { "content-type": "application/x-www-form-urlencoded" },
      method: 'POST',
      data: {
        title:that.data.title,
        body:that.data.body,
        picture:that.data.picture,
        privacy:'1'
      },
      success: function(res) {
        console.log(res.data)
        if(res.data!='表单内容有误，请重新填写。'){
          that.setData({
            showOneButtonDialog1:true
          });

        }
        else{
          that.setData({
            showOneButtonDialog2:true
          });
        }
      }
    })
    
  },
  get_detail: function(){
    var that = this;
    var url="http://127.0.0.1:8000/article/article_detail/"+that.data.article_id; //结合登入后，后台验证是否获得私密发布，request.user.id
    wx.request({
      url: url,
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        console.log(res.data)
        console.log(res)
        console.log(typeof(res.data))
        that.setData({
          result:res.data[0],
          body:res.data[0]['body'],
          title:res.data[0]['title']

        })
      }
    })
  },
  article_update_open: function(){
    var that = this;
    var url="http://127.0.0.1:8000/article/article_update/"+that.data.article_id+'/'; 
    wx.request({
      url: url,
      method:'POST',
      header: { "content-type": "application/x-www-form-urlencoded" },
      data: {
        title:that.data.title,
        body:that.data.body,
        picture:that.data.picture,
        privacy:'0'
      },
      
      success: function(res) {
        console.log(res.data)
        console.log(res)
        console.log(typeof(res.data))
        that.setData({
          showOneButtonDialog3:true
        })
        
      }
    })
  },
  article_update_privacy: function(){
    var that = this;
    var url="http://127.0.0.1:8000/article/article_update/"+that.data.article_id+'/'; 
    wx.request({
      url: url,
      method:'POST',
      header: { "content-type": "application/x-www-form-urlencoded" },
      data: {
        title:that.data.title,
        body:that.data.body,
        picture:that.data.picture,
        privacy:'1'
      },
      
      success: function(res) {
        console.log(res.data)
        console.log(res)
        console.log(typeof(res.data))
        that.setData({
          showOneButtonDialog3:true
        })
      }
    })
  },
  
  input_body:function(e){
    this.setData({
      body:e.detail.value
    })
  },
  input_title:function(e){
    this.setData({
      title:e.detail.value
    })
  },
  open:function(e){
    this.setData({'open':true})
    this.upload(e);
  },
  ceshi:function(e){
    wx.request({
      url: 'http://127.0.0.1:8000/article_create/',
      header: { "content-type": "application/x-www-form-urlencoded" },
      method: 'POST',
      success: function(res) {console.log(res.data)}
    })
  }
})