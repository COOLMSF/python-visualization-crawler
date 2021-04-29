<template>
  <div id="centreRight1">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span style="color:#5cd9e8">
          <icon name="chart-line"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2">任务完成排行榜</span>
        </div>
      </div>
      <div class="d-flex jc-center body-box">
        <dv-scroll-board :config="config" style="width:3.375rem;height:4.28rem" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      config: {
        header: ["话题", "变化率"],
        data: [
          ["tin宝",  "<span  class='colorGrass'>↑7%</span>"],
          ["恋与制作人",  "<span  class='colorRed'>↓3%</span>"],
          ["苏芮琪",  "<span  class='colorGrass'>↑1%</span>"],
          ["黄明昊",  "<span  class='colorGrass'>↑1%</span>"],
          ["印度新冠",  "<span  class='colorGrass'>↑5%</span>"],
          ["美国制裁",  "<span  class='colorGrass'>↑3%</span>"],
          ["易烊千玺",  "<span  class='colorGrass'>↑4%</span>"],
          ["王者荣耀",  "<span  class='colorRed'>↓4%</span>"],
          ["和平精英",  "<span  class='colorRed'>↓1%</span>"],
        ],
        rowNum: 7, //表格行数
        headerHeight: 35,
        headerBGC: "#0f1325", //表头
        oddRowBGC: "#0f1325", //奇数行
        evenRowBGC: "#171c33", //偶数行
        index: true,
        columnWidth: [50],
        align: ["center"]
      }
    };
  },
  components: {},
  mounted() {},
  methods: {}
};
</script>

<style lang="scss">
#centreRight1 {
  padding: 0.2rem;
  height: 5.125rem;
  min-width: 3.75rem;
  border-radius: 0.0625rem;
  .bg-color-black {
    height: 4.8125rem;
    border-radius: 0.125rem;
  }
  .text {
    color: #c3cbde;
  }
  .body-box {
    border-radius: 0.125rem;
    overflow: hidden;
  }
}
</style>
