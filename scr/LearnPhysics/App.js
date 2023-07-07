import { StatusBar } from 'expo-status-bar';
import { SafeAreaView, StyleSheet, Text, Button, Image } from 'react-native';


const pressButton = () => console.log('Click');

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text>Hello!!!</Text>

      <Button title='Press Me' color='red' onPress={pressButton}/>

      <Image source={require('/assets/adaptive-icon.png')} />

      <StatusBar style="auto" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});
