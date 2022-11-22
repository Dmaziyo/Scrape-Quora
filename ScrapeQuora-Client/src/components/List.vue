<template>
  <div class="list">
    <div v-for="(item, index) in list" :key="index" class="list-item">
      <div class="list-info">
        <a :href="item.href">
          <h2 class="title">{{ item.title }}</h2>
          <p class="desc">{{ item.p }}</p>
        </a>
        <div class="heat_font">
          <img src="static/images/heat.svg" alt />
          <span>{{ item.heat }}</span>
        </div>
      </div>
      <img v-if="item.img" class="list-pic" :src="item.img" />
    </div>
  </div>
</template>

<script>
/**
 * heat: "1740 万热度​分享"
 * href: "https://www.zhihu.com/question/544720946"
 * img: "https://pic2.zhimg.com/80/v2-12fcebac87705d496f6c34552a8c1fe7_400x224.png"
 * p: "据侠客岛，在南京的寺庙供奉日本侵华战犯牌位，置几十万大屠杀冤魂于何地？！此事严重伤害中国人民的感情，简直就是侮辱。当地已回应，称将对此事一查到底。岛叔想说，这次事件是寺庙只顾收钱办事、管理不严，还是有人故意为之、甚至有更隐秘的情况，以及那个「吴啊萍」究竟
 * title: "侠客岛称「须严查南京寺庙供奉日本战犯一事」，供奉者「吴啊萍」究竟是谁？相关方可能会受到哪些处罚？"
 */
//引入axios接口
import axios from "axios";
export default {
  data() {
    return {
      //此处返回一个数组list
      list: [],
    };
  },
  mounted() {
    this.getlist();
  },
  methods: {
    getlist() {
      axios.get("/hot").then((res) => {
        this.list = res.data.msg.data;
      });
    },
  },
};
</script>

<style scoped>
.list-item {
  display: flex;
  padding: 20px 0;
  overflow: hidden;
  border-bottom: 1px solid #dcdcdc;
}
.list-pic {
  width: 190px;
  height: 105px;
  display: block;
  border-radius: 4px;
}
.list-info {
  width: 500px;
}
.list-info a {
  text-decoration: none;
  overflow: hidden;
  text-overflow: ellipsis;
}
.title {
  overflow: hidden;
  text-overflow: ellipsis;
  max-height: 56px;
  padding: 10px 0;
  font-size: 18px;
  font-weight: bold;
  color: #333;
}
.heat_font {
  display: flex;
  font-size: 14px;
  color: #8590a6;
  height: 16px;
}
.desc {
  line-height: 22px;
  font-size: 13px;
  color: #444;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>
