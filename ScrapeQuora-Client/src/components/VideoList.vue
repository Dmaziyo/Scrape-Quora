<template>
  <div class="video-list">
    <div v-for="(item, index) in videoList" :key="index" class="video-item">
      <a target="_blank" :href="item.href">
        <div class="video-poster">
          <img class="poster" :src="item.img" alt="" />
          <div class="video-detail">
            <div class="views">
              <img src="static/images/play.svg" alt="" />
              <span>{{ item.views }}</span>
            </div>
            <div class="timeline">{{ item.v_time }}</div>
          </div>
        </div>
      </a>
      <h2 class="title">
        <a :href="item.href">{{ item.title }}</a>
      </h2>
      <div class="creator-detail">
        <a class="icon-detail" :href="item.href">
          <div class="icon">
            <img :src="item.creator_icon" alt="" />
          </div>
          <div class="creator-name">{{ item.creator }}</div>
        </a>
        <div class="more">
          <img src="static/images/more.svg" alt="" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "videoList",
  data() {
    return {
      //此处返回一个数组list
      videoList: [],
    };
  },
  mounted() {
    this.getVideoList();
  },
  methods: {
    getVideoList() {
      axios.get("/video").then((res) => {
        this.videoList = res.data.msg.data;
      });
    },
  },
};
</script>

<style lang="less">
.video-list {
  display: flex;
  flex-wrap: wrap;
  width: 694px;
  margin: 0 auto;
}
.video-item {
  width: 207px;
  min-height: 205px;
  margin: 0px 16.5px 32px 0px;
  a {
    text-decoration: none;
    color: black;
  }
  .video-poster {
    position: relative;
    cursor: pointer;
    width: 100%;
    height: 128px;
    border-radius: 4px;
    overflow: hidden;
  }
  .poster {
    position: absolute;
    object-fit: cover;
    height: 100%;
  }
  .video-detail {
    display: flex;
    width: 100%;
    height: 25px;
    position: absolute;
    left: 0px;
    bottom: 0px;
    justify-content: space-between;
    color: white;
    font-size: 12px;
    line-height: 25px;
    background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%);
  }
  .title {
    font-size: 14px;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
  }
  .creator-detail {
    display: flex;
    justify-content: space-between;
    a {
      display: flex;
    }
    .icon {
      width: 15px;
      img {
        width: 100%;
        border-radius: 50%;
      }
    }
    .creator-name {
      font-size: 12px;
      color: rgb(100, 100, 100);
    }
  }
}
</style>
