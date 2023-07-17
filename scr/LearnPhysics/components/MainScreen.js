import React from 'react';
import { StyleSheet, View, Text, Button} from 'react-native';


export default function Main() {
  return (
    <View>
      <Text style={styles.text}> Learn Physics </Text>
      <Button />
    </View>
  );
}


const styles = StyleSheet.create({
    text: {
        flex: 1,
        width: '500%',
        textAlign: 'center',
        color: '#1976d2',
        backgroundColor: '#c3c3c3'
    }
});
