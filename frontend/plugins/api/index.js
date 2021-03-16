import vision from './modules/vision'

export default ({ $axios }, inject) => {
  const client = $axios

  client.vision = vision(client)

  inject('request', client)
}
