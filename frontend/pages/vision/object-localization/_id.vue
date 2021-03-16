<template>
  <v-row>
    <v-col :sm="12" :md="6">
      <img :src="image.result" width="100%" alt="">
    </v-col>
    <v-col height="300px">
      <json-viewer :value="image.jsonContent" :expand-depth="5" min-height="300px" max-height="500px" />
    </v-col>
  </v-row>
</template>
<script>
export default {
  async asyncData (context) {
    try {
      const image = await context.app.$request.vision.object_localization.get(context.params.id)
      return { image }
    } catch (error) {
      return { image: [] }
    }
  }
}
</script>
