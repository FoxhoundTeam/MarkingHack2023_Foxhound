<!--
  работа со схемами в SVG
  применение: пульты, индикация состояния промышленных установок
  особенности:
  - SVG необходимо грузить через тек <object>, а не <img>, иначе элементы
  рисунка будут недоступны в DOM
  - работу с элементами SVG (анимирование) можно производить через DOM
  - редакторы могут сохранять теги SVG каждый раз по-разному (например,
  вместо <text> сохранять <svg:text>), поэтому при обращении к DOM после
  каждого сохранения надо уточнять теги
-->

<template>
  <!-- <v-row
    class="pa-1 yellow fill-height"
    style="height: 100%;"
  > -->
  <v-row

  >
    <!-- <v-col
      cols="12" md="6" class="pa-1 red fill-height"
      style="height: 100%;"
    > -->
    <v-col

      >
      <v-card
        >

      </v-card>
    </v-col>
    <v-col cols="12" md="6"></v-col>
  </v-row>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'LoginView',
  data(){
    return {
      list_model: Array(50).fill("x"),//["элемент"]*100;
    }
  },

  beforeCreate(){},

  created() {},

  beforeMount(){},

  mounted() {},

  computed: {},

  watch: {},
}
</script>
