export default function (client) {
  return {
    object_localization: {
      list () {
        return client.$get('vision/object_localization/')
      },
      get (id) {
        return client.$get(`vision/object_localization/${id}`)
      }
    }
  }
}
