import React from 'react';
import Main from '../components/MainScreen';
import Second from '../components/SecondScreen';

import { createStackNavigation } from '@react-navigation/stack';
import { NavigationContainer  } from '@react-navigation/native';

const Stack = createStackNavigation();

export default function NewNavigation(){
    <NavigationContainer>
        <Stack.Navigator>
            <Stack.Screen 
                name="Main"
                component={Main}
                options={{title: 'Home'}}
            />
            <Stack.Screen 
                name="Second"
                component={Second}
                options={{title: 'NEW'}}
            />
        </Stack.Navigator>
    </NavigationContainer>
}