<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue';
export default {
  data () {
    return {
      cdata: {
        xData: ["tin宝", "恋与制作人", "苏芮琪", "黄明昊", "印度新冠", "美国制裁"],
        seriesData: [
          { value: 10, name: "rtin宝" },
          { value: 5, name: "恋与制作人" },
          { value: 15, name: "苏芮琪" },
          { value: 25, name: "黄明昊" },
          { value: 20, name: "印度新冠" },
          { value: 35, name: "美国制裁" }
        ]
      }
    }
  },
  components: {
    Chart,
  },
  mounted () {
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
</style>
