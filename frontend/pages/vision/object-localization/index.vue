<template>
  <v-row class="mt-4 mb-4 pa-3">
    <!-- 一覧表示 -->
    <v-col v-for="(image,i) in images" :key="i" :cols="12" :sm="6" :md="4">
      <v-card class="lighten-3 ma-2">
        <!-- 詳細ページのリンク -->
        <nuxt-link :to="`/vision/object-localization/${image.id}`">
          <v-card-text><img :src="image.result" width="100%" alt=""></v-card-text>
        </nuxt-link>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
export default {
  // コンポーネントへのデータ登録
  async asyncData (context) {
    try {
      // 登録したplagin の利用
      const images = await context.app.$request.vision.object_localization.list()
      console.log({
        images
      })
      return { images }
    } catch (e) {
      console.log(e)
      return { images: [] }
    }
  }
}
</script>
