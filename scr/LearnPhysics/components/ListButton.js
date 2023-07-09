import React from 'react';
import { StyleSheet, TouchableOpacity, Text } from 'react-native';


export default function ListItem({ elem }) {
  return (
    <TouchableOpacity>
      <Text> {elem.text} </Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({

});